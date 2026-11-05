# Configuración observada en T1 y T2

Los archivos `environment.json` y `models_before.json` de ambas corridas registran:

| Campo | Valor observado |
|---|---|
| Sistema | Linux `7.0.0-38-generic-x86_64-with-glibc2.39` |
| Python del registrador | 3.12.3 |
| Zona horaria del registro | `America/Lima` |
| API de LM Studio | `http://127.0.0.1:1234` |
| Modelo cargado | `qwen/qwen3.5-9b`, variante `qwen/qwen3.5-9b@q4_k_m` |
| Formato y cuantización | GGUF, Q4_K_M |
| Contexto de la instancia cargada | 39 680 tokens |
| Límite temporal configurado | 120 s |
| MCP esperado por el registrador | `http://127.0.0.1:39280/mcp` |

La dirección MCP es la **esperada** según el registro, no una copia verificada de `mcp.json`. La presencia de otros modelos en `models_before.json` no significa que se usaran en estas corridas. Los registros consultados no acreditan la versión exacta de LM Studio, la versión de FreeCAD ni el hardware completo; esos campos quedan sin completar.

El contexto de 32 768 tokens mencionado en conversaciones de planificación no es el valor de la instancia cargada en T1/T2. Para esas dos corridas prevalece el valor de 39 680 registrado por LM Studio.
