#!/usr/bin/env python3
"""Cronómetro manual y muestreo de recursos durante una prueba de LM Studio."""

import argparse
import csv
import datetime as dt
import os
import pathlib
import subprocess
import threading
import time
import uuid


ROOT = pathlib.Path(__file__).resolve().parent
SAMPLE_FIELDS = (
    "run_id", "mode", "timestamp_local", "elapsed_seconds", "gpu_name",
    "gpu_total_mib", "gpu_used_mib", "gpu_util_percent", "gpu_temp_c",
    "gpu_power_w", "llama_pid", "llama_gpu_mib", "llama_rss_mib", "llama_cpu_percent",
    "system_mem_available_mib",
)


def command_output(*args):
    try:
        return subprocess.run(args, capture_output=True, text=True, timeout=5, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ""


def as_float(value):
    try:
        return float(value.strip().split()[0])
    except (ValueError, IndexError, AttributeError):
        return None


def llama_process():
    output = command_output(
        "nvidia-smi", "--query-compute-apps=pid,process_name,used_gpu_memory",
        "--format=csv,noheader,nounits",
    )
    for line in output.splitlines():
        parts = [part.strip() for part in line.split(",", 2)]
        if len(parts) == 3 and "llama-server" in parts[1]:
            return parts[0], as_float(parts[2])
    return "", None


def process_rss_mib(pid):
    if not pid:
        return None
    try:
        for line in pathlib.Path(f"/proc/{pid}/status").read_text().splitlines():
            if line.startswith("VmRSS:"):
                return float(line.split()[1]) / 1024
    except (OSError, ValueError, IndexError):
        pass
    return None


def process_cpu_ticks(pid):
    if not pid:
        return None
    try:
        fields = pathlib.Path(f"/proc/{pid}/stat").read_text().rpartition(")")[2].split()
        return int(fields[11]) + int(fields[12])
    except (OSError, ValueError, IndexError):
        return None


def available_ram_mib():
    try:
        for line in pathlib.Path("/proc/meminfo").read_text().splitlines():
            if line.startswith("MemAvailable:"):
                return float(line.split()[1]) / 1024
    except (OSError, ValueError, IndexError):
        pass
    return None


def sample(run_id, mode, start):
    output = command_output(
        "nvidia-smi",
        "--query-gpu=name,memory.total,memory.used,utilization.gpu,temperature.gpu,power.draw",
        "--format=csv,noheader,nounits",
    )
    gpu = [part.strip() for part in output.splitlines()[0].split(",")] if output else []
    gpu += [""] * (6 - len(gpu))
    pid, llama_gpu_mib = llama_process()
    return (
        run_id, mode, dt.datetime.now().astimezone().isoformat(),
        round(time.perf_counter() - start, 3), gpu[0],
        as_float(gpu[1]), as_float(gpu[2]), as_float(gpu[3]),
        as_float(gpu[4]), as_float(gpu[5]), pid,
        llama_gpu_mib, process_rss_mib(pid), None, available_ram_mib(),
    )


def monitor(stop, rows, run_id, mode, start):
    previous_pid = None
    previous_ticks = None
    previous_time = None
    ticks_per_second = os.sysconf("SC_CLK_TCK")
    while not stop.is_set():
        row = list(sample(run_id, mode, start))
        now = time.perf_counter()
        ticks = process_cpu_ticks(row[10])
        if row[10] == previous_pid and ticks is not None and previous_ticks is not None:
            elapsed = now - previous_time
            if elapsed > 0:
                row[13] = max(0.0, 100 * (ticks - previous_ticks) / (ticks_per_second * elapsed))
        rows.append(tuple(row))
        previous_pid, previous_ticks, previous_time = row[10], ticks, now
        stop.wait(2)


def peak(rows, index):
    values = [row[index] for row in rows if isinstance(row[index], (int, float))]
    return max(values) if values else None


def write_csv(path, header, rows):
    write_header = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if write_header:
            writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("think_on", "think_off"))
    args = parser.parse_args()
    run_id = uuid.uuid4().hex[:8]

    print("Deja el prompt pegado en LM Studio, listo para enviarlo.")
    input("Pulsa Enter aquí e inmediatamente envía el prompt...")
    start_wall = dt.datetime.now().astimezone()
    start = time.perf_counter()
    stop = threading.Event()
    rows = []
    worker = threading.Thread(target=monitor, args=(stop, rows, run_id, args.mode, start), daemon=True)
    worker.start()
    try:
        input("Cuando termine la respuesta final, vuelve aquí y pulsa Enter...")
    finally:
        seconds = time.perf_counter() - start
        end_wall = dt.datetime.now().astimezone()
        stop.set()
        worker.join(timeout=8)

    write_csv(ROOT / "resultados_tiempo.csv",
              ("run_id", "task", "mode", "start_local", "end_local", "wall_seconds"),
              [(run_id, "T4_complex", args.mode, start_wall.isoformat(), end_wall.isoformat(), f"{seconds:.3f}")])
    write_csv(ROOT / "resultados_recursos.csv", SAMPLE_FIELDS, rows)

    print(f"Tiempo total: {seconds:.3f} s ({seconds / 60:.2f} min)")
    print(f"Muestras de recursos: {len(rows)}")
    print(f"Pico de VRAM del proceso Qwen: {peak(rows, 11)} MiB")
    print(f"Pico de RAM del proceso: {peak(rows, 12)} MiB (RSS; puede incluir memoria mapeada)")
    print(f"Pico de uso de GPU: {peak(rows, 7)} %")
    print(f"Pico de CPU del proceso: {peak(rows, 13)} % (100 % equivale a un núcleo)")
    print(f"Archivos: {ROOT / 'resultados_tiempo.csv'} y {ROOT / 'resultados_recursos.csv'}")


if __name__ == "__main__":
    main()
