# Tamaño y recursos de Qwen3.5-9B en Hinton1

Medición puntual: 2026-10-29, aproximadamente 13:29–13:30 (America/Lima). Estos números describen el modelo cargado en ese momento, **no** un pico de una corrida Think ON/OFF.

| Concepto | Valor observado |
|---|---:|
| Modelo GGUF | `Qwen3.5-9B-Q4_K_M.gguf` |
| Cuantización | Q4_K_M |
| Tamaño exacto del archivo principal | 5 627 044 256 bytes = 5.627 GB = 5.241 GiB |
| Archivo de visión separado (`mmproj`, si se usa) | 921 704 480 bytes = 0.922 GB = 0.858 GiB |
| GPU | NVIDIA RTX A6000, 49 140 MiB de VRAM total |
| VRAM del proceso `llama-server` | 7 484 MiB ≈ 7.31 GiB |
| VRAM total ocupada por todos los procesos | 8 229 MiB ≈ 8.04 GiB |
| Memoria residente del proceso `llama-server` | ~10.6 GiB RSS/PSS |
| GPU ocupada en ese instante | 13 % |
| Temperatura / potencia GPU | 41 °C / 29.91 W |
| RAM del equipo | 31 GiB total, ~9.9 GiB disponible en ese instante |

El tamaño del GGUF es almacenamiento en disco. La VRAM del proceso proviene de `nvidia-smi --query-compute-apps`; la VRAM total ocupada incluye escritorio y otras aplicaciones. RSS/PSS son medidas de memoria del proceso en Linux y pueden incluir regiones mapeadas; no deben sumarse directamente a la VRAM como si fueran recursos independientes. No se confirmó si el archivo `mmproj` estaba cargado, por lo que se reporta por separado.

Durante las dos corridas pareadas, `benchmark_timer.py` muestrea cada dos segundos la VRAM del proceso, uso total de GPU, utilización, temperatura, potencia, RSS, CPU del proceso y RAM disponible. El porcentaje de CPU usa 100 % como un núcleo completo y puede superar 100 % si el proceso usa varios núcleos. Los tiempos van a `resultados_tiempo.csv`; todas las muestras van a `resultados_recursos.csv`, vinculadas por `run_id`. Los máximos muestreados son aproximaciones a los picos reales.
