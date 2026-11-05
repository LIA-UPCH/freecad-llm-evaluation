# Metodología de evaluación

## Objetivo

Evaluar si un modelo de lenguaje ejecuta tareas CAD mediante FreeCAD MCP y entrega un artefacto que cumple una especificación geométrica. Registrar aparte la fiabilidad de la integración y la exactitud de lo que el asistente afirma haber hecho.

## Unidad de análisis

Cada intento requiere un prompt, identificación del modelo y su configuración, registro de llamadas MCP, tiempo definido desde el envío de la solicitud hasta el fin de la respuesta, archivo de salida y una verificación independiente. Las consultas de preparación no cuentan como intentos CAD.

Para futuras comparaciones, iniciar cada intento en un documento nuevo, mantener constantes prompt y parámetros, guardar también los fallos y repetir cada tarea antes de calcular tasas de éxito. El plan de repeticiones no debe confundirse con las dos corridas disponibles.

## Criterios de aceptación

1. **Existencia:** el archivo esperado está guardado y puede abrirse.
2. **Integridad:** contiene geometría no vacía y exactamente un sólido final válido.
3. **Especificación:** dimensiones, ubicación y diámetro de todos los taladros coinciden con el prompt; cada taladro atraviesa el espesor.
4. **Presentación:** el sólido final es identificable y los objetos auxiliares no confunden el resultado. Este punto se registra aparte del cumplimiento geométrico.

La respuesta textual del modelo, el estado HTTP/MCP y el archivo `.FCStd` se examinan por separado. Las excepciones emitidas en `stderr` se cuentan aunque el envoltorio de la llamada marque `success`. Los tokens y tiempos se citan solo cuando figuran en los registros.

## Tareas documentadas

- **T1:** bloque de 40 × 30 × 10 mm, agujero pasante de Ø8 mm centrado en (20, 15).
- **T2:** placa de 60 × 40 × 8 mm, cuatro agujeros pasantes de Ø5 mm centrados en (8, 8), (52, 8), (8, 32) y (52, 32).

Volúmenes de referencia, calculados a partir de la especificación: T1 = 12 000 − 160π ≈ 11 497,345 mm³; T2 = 19 200 − 200π ≈ 18 571,681 mm³. Un volumen correcto no basta para validar la posición de los agujeros.
