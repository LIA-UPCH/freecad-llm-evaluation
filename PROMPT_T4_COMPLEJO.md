# T4: prueba pareada Think ON / Think OFF

Usar **exactamente el mismo prompt** en dos chats nuevos de LM Studio con `qwen/qwen3.5-9b` y FreeCAD MCP activo. En la primera corrida, Think ON; en la segunda, Think OFF. Mantener iguales modelo, cuantización, contexto, temperatura, GPU offload y demás ajustes. No pegar chats previos al modelo. Si `T4_complex_run` ya existe en FreeCAD, el prompt pide un nombre único, por lo que no se altera la primera ejecución.

```text
Execute this task in FreeCAD using the available MCP tools.

Create a NEW document named T4_complex_run. If that name already exists, choose a unique name. Do not modify or close any existing document.

Model a 80 × 50 × 8 mm rectangular plate extending from (0, 0, 0) to (80, 50, 8).

Add four cylindrical through-holes, each 6 mm in diameter, parallel to the Z axis and centered at these XY coordinates in millimeters:
(10, 10), (70, 10), (10, 40), and (70, 40).

Also cut a centered rectangular blind pocket into the top face. Its X boundaries must be 25 to 55 mm, its Y boundaries must be 15 to 35 mm, and its flat bottom must be at Z = 5 mm. The pocket is therefore 30 × 20 mm and 3 mm deep; it must not pass through the plate. The pocket must not intersect any through-hole.

Use a Part::Box for the base, four separate Part::Cylinder objects for the holes, a separate Part::Box for the pocket tool, and Boolean cuts for the finished part. Keep all construction objects and Boolean operations in the document with their dependencies intact. Hide intermediate objects and show only the final part.

Recompute the document, set an isometric view, and fit the final part in the viewport. Verify shape validity, exactly one solid, outer dimensions, all four hole diameters and positions, the pocket position and depth, and the expected volume of approximately 29295.221316 mm³. A matching volume alone is not sufficient to verify feature positions.

Actually execute the task using the available tools. Report the document name, objects created, checks actually computed, and any failed tool calls. Do not claim a check passed unless it was computed from the final model.
```

## Registro

Antes de enviar cada prompt, iniciar `python3 benchmark_timer.py think_on` o `python3 benchmark_timer.py think_off` en una terminal desde esta carpeta. Tener el prompt ya pegado en LM Studio, pulsar Enter en el cronómetro y enseguida enviar el prompt. Al terminar la respuesta final del modelo, volver a la terminal y pulsar Enter. El script escribe `resultados_tiempo.csv` y `resultados_recursos.csv`. La medición puntual inicial de tamaño y recursos está en `RECURSOS_QWEN.md`.

Guardar para cada corrida: conversación exportada, `.FCStd`, captura, nombre interno del documento, ajustes del modelo, número de llamadas y errores de herramientas, salida de verificación independiente, y tiempo de pared. Con una sola corrida por modo, los resultados son **exploratorios**, no una estimación robusta del efecto de Think.

Volumen esperado: `80*50*8 - 4*pi*3^2*8 - 30*20*3 ≈ 29295.22131576614` mm³.
