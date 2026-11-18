# Evaluación de modelos de lenguaje en FreeCAD

Este repositorio reúne las pruebas de un estudio sobre el uso de modelos de lenguaje de pesos abiertos para crear piezas en FreeCAD. Las tareas se ejecutan desde LM Studio mediante un servidor MCP y luego se revisan en FreeCAD.

## Cómo se evalúan las piezas

Cada tarea indica las dimensiones y operaciones que debe tener la pieza. Después de la ejecución, se revisan la validez de la forma, el número de sólidos, las dimensiones y las dependencias entre objetos. Cuando hay una pieza final, también se compara con una geometría de referencia construida por separado.

## Pruebas realizadas

| Prueba | Tarea | Resultado |
| --- | --- | --- |
| T1 | Placa con un agujero central | La geometría coincidió con la referencia, pero el corte quedó inválido al eliminarse sus objetos de construcción. |
| T2 | Placa con cuatro agujeros | La geometría coincidió con la referencia. Se conservaron los cortes, aunque la placa base no es paramétrica editable. |
| T3 | Placa con un bolsillo ciego | La pieza es válida y tiene el volumen esperado, pero el bolsillo quedó desplazado. |
| T4 | Placa con agujeros y bolsillo | La corrida con Think ON terminó sin una pieza final verificable, después de errores y tiempos de espera. |

## Entorno de prueba

Las pruebas documentadas se realizaron con Qwen3.5-9B en formato GGUF Q4_K_M, LM Studio 0.4.26+4, FreeCAD 1.1.1 y una GPU NVIDIA RTX A6000 de 48 GB. Los detalles del modelo y las mediciones disponibles están en [RECURSOS_QWEN.md](RECURSOS_QWEN.md).

## Archivos

- [CONTINUIDAD.md](CONTINUIDAD.md): notas de trabajo, resultados y verificaciones de cada prueba.
- [PROMPT_T4_COMPLEJO.md](PROMPT_T4_COMPLEJO.md): tarea y protocolo para la comparación de T4.
- [evidencia/T1](evidencia/T1/): conversación y archivo de FreeCAD de T1.
- [benchmark_timer.py](benchmark_timer.py): cronómetro y registro de recursos. Los datos guardados están en [resultados_tiempo.csv](resultados_tiempo.csv) y [resultados_recursos.csv](resultados_recursos.csv).
- [Documentación completa y evidencias](freecad-evaluacion-documentacion-completa.zip): incluye los archivos de T1 a T4, capturas y el borrador del artículo. Las carpetas de T2 a T4 y el artículo se encuentran dentro del ZIP.

## Pendiente

Completar T4 con Think OFF, verificar la pieza resultante y repetir las pruebas con una configuración registrada de forma consistente. Más adelante se podrán añadir otros modelos y tareas.

## Referencias

- [FreeCAD](https://github.com/FreeCAD/FreeCAD)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)
- [Qwen3.5-9B-GGUF](https://huggingface.co/lmstudio-community/Qwen3.5-9B-GGUF)
