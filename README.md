# Evaluación de modelos de lenguaje para FreeCAD

Investigación exploratoria sobre el uso de modelos de lenguaje de pesos abiertos para ejecutar tareas de modelado paramétrico en FreeCAD mediante herramientas conectadas por Model Context Protocol (MCP).

El proyecto estudia si las piezas generadas cumplen las dimensiones y restricciones solicitadas, y si conservan una estructura de operaciones válida y editable. La evaluación distingue entre lo que informa el modelo y lo que se verifica de manera independiente en FreeCAD.

> **Estado:** estudio piloto en curso. Los resultados documentados corresponden a un modelo y a un número reducido de ensayos; no representan una estimación estadística de fiabilidad.

## Entorno evaluado

- **Modelo:** Qwen3.5-9B, formato GGUF Q4_K_M.
- **Ejecución:** LM Studio 0.4.26+4 y servidor MCP para FreeCAD.
- **CAD:** FreeCAD 1.1.1.
- **Hardware:** NVIDIA RTX A6000 de 48 GB.

Los detalles disponibles sobre el modelo, la memoria y las mediciones se encuentran en [RECURSOS_QWEN.md](RECURSOS_QWEN.md) y [CONTINUIDAD.md](CONTINUIDAD.md).

## Método de evaluación

Cada tarea define una geometría, dimensiones, posiciones y operaciones esperadas. Se conservan los prompts, las conversaciones y los archivos de FreeCAD disponibles. La revisión independiente considera:

1. Validez de la forma y número de sólidos.
2. Dimensiones, ubicación y profundidad de las operaciones.
3. Correspondencia con una referencia geométrica construida por separado, mediante diferencias booleanas.
4. Conservación de objetos y dependencias necesarios para editar el modelo.
5. Tiempo, recursos y errores registrados cuando están disponibles.

## Resultados preliminares

| Caso | Tarea | Resultado observado |
| --- | --- | --- |
| T1 | Placa con agujero central | Geometría correcta, pero corte paramétrico inválido por dependencias eliminadas. |
| T2 | Placa con cuatro agujeros | Coincidencia geométrica verificada; la placa base no es paramétrica editable. |
| T3 | Placa con bolsillo ciego | Pieza válida y volumen esperado, pero bolsillo desplazado. |
| T4 | Placa con agujeros y bolsillo, Think ON | Ejecución incompleta tras errores y tiempos de espera; no hay pieza final verificada. |

La comparación de T4 con **Think OFF** sigue pendiente. Las ejecuciones incluyen reintentos y no permiten atribuir diferencias a ese modo ni calcular una tasa de éxito general.

## Contenido del repositorio

- [CONTINUIDAD.md](CONTINUIDAD.md): contexto, protocolo, verificaciones y estado de las pruebas.
- [PROMPT_T4_COMPLEJO.md](PROMPT_T4_COMPLEJO.md): tarea y protocolo propuesto para la comparación de T4.
- [RECURSOS_QWEN.md](RECURSOS_QWEN.md): información del modelo y mediciones del entorno.
- [evidencia/T1/](evidencia/T1/): conversación y modelo de FreeCAD de T1.
- [benchmark_timer.py](benchmark_timer.py), [resultados_tiempo.csv](resultados_tiempo.csv) y [resultados_recursos.csv](resultados_recursos.csv): cronometraje y registro de recursos.
- [Paquete completo de documentación y evidencias](freecad-evaluacion-documentacion-completa.zip): archivos originales de T1–T4, capturas, modelos y borrador del artículo. Descarga y descomprime el ZIP para consultar las carpetas de T2–T4 y el artículo.

## Próximos pasos

- Completar la prueba T4 con Think OFF en una sesión nueva y verificar la geometría independientemente.
- Registrar de forma consistente la configuración y repetir los ensayos por condición.
- Ampliar las tareas y evaluar otros modelos de pesos abiertos con el mismo protocolo.

## Referencias

- [FreeCAD](https://github.com/FreeCAD/FreeCAD)
- [Model Context Protocol: arquitectura](https://modelcontextprotocol.io/docs/learn/architecture)
- [Qwen3.5-9B-GGUF en Hugging Face](https://huggingface.co/lmstudio-community/Qwen3.5-9B-GGUF)
