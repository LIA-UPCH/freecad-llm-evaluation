# Evaluación de LLM con FreeCAD y MCP

Este repositorio documenta ensayos de modelado paramétrico realizados con Qwen local mediante LM Studio y FreeCAD MCP. Se evalúan por separado la respuesta del asistente, las llamadas a herramientas y el archivo CAD guardado.

## Estado de la evidencia

Hay dos corridas documentadas de Qwen3.5-9B, una de T1 y una de T2, ambas del 30 de octubre de 2026. Los archivos `.FCStd` y los prompts originales están en [evidence/freecad](evidence/freecad). La lectura de sus registros está en [resultados T1/T2](docs/resultados-t1-t2.md). No constituyen una comparación estadística entre modelos ni varias repeticiones.

El caso [KiCad NE555](docs/kicad-ne555.md) cuenta con una especificación reconstruida. Aquí no hay proyecto KiCad, registros de ejecución ni informes ERC/DRC para declararlo completado.

## Documentación

- [Metodología y criterios de verificación](docs/metodologia.md)
- [Configuración observada](docs/configuracion.md)
- [Resultados y procedencia de T1/T2](docs/resultados-t1-t2.md)
- [Especificación KiCad NE555](docs/kicad-ne555.md)

Una respuesta `completed` del servidor o un archivo guardado no demuestran por sí solos que la geometría cumpla la consigna.
