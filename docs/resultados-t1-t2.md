# Resultados observados: T1 y T2

Fuente primaria: `D:/CIP_LLM/T1.zip` y `D:/CIP_LLM/T2.zip`, revisados para esta propuesta. Se incorporan los prompts exactos y los archivos `.FCStd` extraídos de esos ZIP. Los registros originales incluyen `summary.json`, `metrics.csv`, `tool_calls.json` y observaciones de `stderr`; la tabla presenta una síntesis para no publicar rutas locales y trazas completas. Las dos consultas contenidas en `registros.zip` son de preparación y no se suman como ensayos.

| Corrida | Tiempo total de solicitud | Llamadas MCP | Errores observados | Estado del archivo CAD |
|---|---:|---:|---:|---|
| T1, Qwen rep01 | 64,246 s | 8 | 7 excepciones en `stderr`; `errors.json` vacío | Auditoría previa del archivo: sólido final conforme, volumen ≈ 11 497,345 mm³; objetos auxiliares visibles. |
| T2, Qwen rep01 | 32,374 s | 5 | 4 errores reportados | Auditoría previa del archivo: tres objetos con geometría vacía; no cumple la consigna. |

En T1, `summary.json` declara `completed` y cero errores observados, mientras `stderr_observations.json` contiene siete excepciones Python. Por ello el estado de la solicitud no equivale a una ejecución limpia. La auditoría previa reportó una pieza final geométricamente conforme; el archivo incluido permite repetir esa comprobación en FreeCAD.

En T2, `summary.json` declara `completed_with_errors`; las cuatro trazas incluyen `Vector` no definido, asignación inválida a un atributo del documento y un error topológico. Aunque la respuesta del asistente anunció éxito, la auditoría previa del `.FCStd` encontró formas vacías. El tiempo mide hasta el fin de la respuesta, no hasta el momento de guardado.

Los resultados geométricos anteriores provienen de una inspección previa documentada en la sesión de elaboración del artículo del laboratorio; en esta propuesta se comprobaron los ZIP, prompts, registros y presencia de los `.FCStd`, pero no se volvió a abrir FreeCAD. La conclusión del artefacto conserva ese alcance explícito.

## Procedencia e integridad

| Archivo | SHA-256 |
|---|---|
| ZIP fuente T1 | `25D5AA9333A2915BEF607BEBD0B506D420FD1A589F059FDD817567F56D617E93` |
| ZIP fuente T2 | `617269FA6D41A304C538DC2A033E5C9C541B3ECB4CCFD492D3A0CF79C4D57005` |
| `evidence/freecad/T1/T1.FCStd` | `8C6C8A978851BB22390DF601A3585B7C79AC98AE169A003B861B7CDC6E1FBFEF` |
| `evidence/freecad/T2/T2.FCStd` | `98ACBF8D5BC1CE78A2B52BD2C420D69E1175EEFDDF9845C1429995F4F62D966E` |

La comparación entre modelos, las tasas de éxito y los intervalos de confianza quedan pendientes de nuevas corridas; estos datos corresponden a **n = 1 por tarea con Qwen**.
