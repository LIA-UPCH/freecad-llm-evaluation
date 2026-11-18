# Evaluación FreeCAD + Qwen — estado al 29 de octubre de 2026

Este archivo sirve para continuar el proyecto sin pegar los chats completos en LM Studio. El repositorio previsto es `LIA-UPCH/freecad-llm-evaluation`; estos archivos locales aún no se han subido a GitHub.

## Entorno y método

- Modelo usado en T2: `qwen/qwen3.5-9b` en LM Studio 0.4.26+4, conectado al servidor MCP de FreeCAD. La estación Hinton1 tiene una NVIDIA RTX A6000 de 48 GB. En la sesión anterior se configuró una ventana de contexto de 32 768 tokens; los números de la interfaz no prueban por sí solos la configuración efectiva de cada ejecución.
- Cada ensayo debe iniciar en un chat nuevo de LM Studio y en un documento nuevo de FreeCAD. No pegar el chat anterior al modelo: conservar su exportación `.md` por separado.
- Guardar prompt, conversación exportada, `.FCStd`, captura, configuración del modelo y verificación independiente. Distinguir los resultados que afirma Qwen de los comprobados en FreeCAD.
- El trabajo actual es exploratorio y el artículo puede presentar avances; no convertir unos pocos ensayos en una tasa de éxito estadísticamente robusta.

## T1 — placa 40 × 30 × 10 mm con agujero central de Ø8 mm

La segunda ejecución de T1 produjo geometría exacta según la verificación independiente hecha en FreeCAD: sólido válido único, límites `(0,40) × (0,30) × (0,10)` mm, eje del agujero en `(20,15)`, volumen `11497.345175425633` mm³ y diferencia booleana con la referencia igual a cero. Sin embargo, el `Part::Cut` final quedó con `Base=None`, `Tool=None` y estado `Touched, Invalid` después de que Qwen borró las piezas de construcción. Esto cuenta como acierto geométrico almacenado, **no** como modelo paramétrico válido. La primera ejecución de T1 también tuvo geometría correcta, pero terminó en un `Part::Feature` sin historial paramétrico. Evidencia copiada en `evidencia/T1/`.

## T2 — placa 60 × 40 × 8 mm con cuatro agujeros de Ø5 mm

Centros pedidos: `(8,8)`, `(52,8)`, `(8,32)`, `(52,32)` mm. El primer intento de T2 en otra conversación falló geométricamente; mantenerlo como intento separado. En el segundo intento, el prompt pidió un documento `T2_run01`; el archivo entregado se llama `T2_run.FCStd`, y FreeCAD mostró que el nombre interno del documento activo era `T2_run01`.

El archivo guardado contiene nueve objetos: una placa base `Part::Feature`, cuatro cilindros `Part::Cylinder`, tres cortes intermedios `Part::Cut` y un `FinalPlate` también `Part::Cut`. Los enlaces `Base` y `Tool` de los cuatro cortes están presentes. Los cilindros tienen radio 2.5 mm, altura 20 mm y comienzan en Z = -10 mm en las cuatro coordenadas requeridas. La placa base no es una caja paramétrica editable.

Verificación independiente ejecutada por el usuario en la consola de FreeCAD:

```text
Documento: T2_run01
Estado: ['Up-to-date']
Valida: True Solidos: 1
Limites: (0.0, 60.0) (0.0, 40.0) (0.0, 8.0)
Volumen real/esperado: 18571.68146928204 18571.68146928204
Sobrante/faltante: 0.0 0.0
Coincidencia: True
```

La referencia independiente fue una caja `60 × 40 × 8` menos cuatro cilindros de radio 2.5 mm. Las dos diferencias booleanas de volumen cero verifican también posición, tamaño y profundidad de los agujeros. La última tabla “PASS” del chat de Qwen usó valores `True` escritos directamente en el código, por lo que no debe presentarse como prueba independiente. Evidencia copiada en `evidencia/T2/`.

## T3 — siguiente ensayo

Objetivo: placa `60 × 40 × 10` mm con un bolsillo rectangular ciego `20 × 12 × 4` mm, desde la cara superior hasta Z = 6 mm, con límites X = 20–40 e Y = 14–26. Volumen esperado: `23040` mm³. Conservar base, herramienta de corte y corte final; ocultar los intermedios. Verificar forma válida, sólido único, caja envolvente, profundidad del bolsillo y coincidencia booleana con una referencia construida aparte.

Prompt en inglés para un chat **nuevo** de LM Studio:

```text
Execute this task in FreeCAD using the available MCP tools.

Create a NEW document named T3_run01. If that name already exists, choose a unique name. Do not modify or close existing documents.

Create a solid plate from (0, 0, 0) to (60, 40, 10) mm.

Cut a centered rectangular blind pocket into the top face:
- Pocket size: 20 mm along X and 12 mm along Y
- Pocket boundaries: X = 20 to 40 mm, Y = 14 to 26 mm
- Pocket depth: 4 mm from the top face, so its flat bottom is at Z = 6 mm
- The pocket must NOT pass through the plate

Use a Part::Box for the base, a separate Part::Box as the pocket cutting tool, and Part::Cut for the finished part. Keep the base and cutting tool in the document, but hide them; show only the finished part. Do not delete the construction objects.

Set an isometric view and fit the part in the viewport. Recompute the document. Verify shape validity, exactly one solid, outer dimensions of 60 × 40 × 10 mm, pocket position and depth, and expected volume of 23,040 mm³.

Actually perform the operations with the tools. Report the document name, objects created, checks actually performed, and any errors. Do not report a check as passed unless it was computed from the model.
```

## T3 — resultado observado

El usuario entregó el archivo `T3_run.FCStd`, el chat exportado y una captura; se copiaron en `evidencia/T3/`. El chat usa el prompt anterior y Qwen reporta `T3_run01` como nombre interno del documento.

La inspección del `.FCStd` muestra tres objetos con enlaces correctos: `Plate_Base` (`Part::Box`, 60 × 40 × 10 mm en el origen), `Pocket_Tool` (`Part::Box`, 20 × 12 × 4 mm) y `Plate_Cut` (`Part::Cut`, `Base=Plate_Base`, `Tool=Pocket_Tool`). Sin embargo, la herramienta está colocada en **(30,20,6)**, por lo que el bolsillo ocupa **X=30–50, Y=20–32, Z=6–10**. El prompt pedía **X=20–40, Y=14–26, Z=6–10**. El centro real es (40,26); el pedido era (30,20). **Clasificación: fallo de posición aunque la operación de corte y el volumen sean plausibles.**

Qwen reportó volumen 23040 mm³, que coincide con el esperado porque el bolsillo conserva las mismas dimensiones. Ese volumen no demuestra que esté centrado. Su verificación final tampoco comprobó validez con `isValid()` ni número de sólidos con `len(Shape.Solids)`; hubo errores de API (`Valid`, `Solid`, `BoundingBox`) y después se infirió éxito de un volumen positivo y de las 11 caras.

Verificación independiente ejecutada por el usuario en la consola de FreeCAD, comparando la pieza con una caja 60 × 40 × 10 menos un bolsillo de 20 × 12 × 4 en `(20,14,6)`:

```text
Estado: ['Up-to-date'] Válida: True Sólidos: 1
Volumen real/esperado: 23039.999999999996 23040.0
Sobrante/faltante frente al bolsillo pedido: 720.0 720.0
```

La pieza es topológicamente válida y tiene el volumen esperado, pero **no coincide con la geometría solicitada**: ambas diferencias booleanas son 720 mm³. T3 queda cerrado como **fallo geométrico por posición incorrecta del bolsillo**, sin modificar la ejecución original.

## Próxima prueba pareada

El usuario propuso comparar Think ON y Think OFF en una tarea más compleja y cronometrar ambas corridas. El prompt idéntico para los dos modos, el protocolo y el volumen esperado están en `PROMPT_T4_COMPLEJO.md`; el cronómetro manual está en `benchmark_timer.py` y guardará los tiempos en `resultados_tiempo.csv`. Esta prueba reemplaza por ahora la propuesta anterior de T4 con una placa en L. Usar chats nuevos y verificar cada pieza de manera independiente antes de comparar éxito y tiempo.

La ficha `RECURSOS_QWEN.md` contiene el tamaño exacto del GGUF Q4_K_M y una medición puntual de VRAM/RAM de Hinton1. El cronómetro ahora también guarda muestras de recursos en `resultados_recursos.csv` cada dos segundos durante las corridas pareadas.

La primera corrida de T4 complejo, etiquetada Think ON, terminó sin pieza final verificable tras múltiples errores y timeouts MCP. Duró 1601.282 s (26 min 41 s). El usuario guardó el documento parcial `T4_complex_run.FCStd`; contiene 51 objetos de múltiples intentos. Evidencia, CSV y análisis en `evidencia/T4/think_on/RESULTADO.md`. Falta la corrida Think OFF; FreeCAD debe reiniciarse antes de empezarla.

## Artículo redactado

El borrador se encuentra en `articulo/Articulo_FreeCAD_Qwen.docx` y su texto editable en `articulo/Articulo_FreeCAD_Qwen.md`. Presenta un estudio piloto de un solo modelo, con resumen, introducción, metodología, tabla de T1–T4, discusión, limitaciones y conclusiones, y tres referencias primarias verificadas. Está configurado en A4, Times New Roman 12, interlineado doble, márgenes de la revista y numeración de páginas. La revisión renderizada ocupa tres páginas. Los datos de autor se dejaron en blanco por indicación expresa del usuario; la comparación Think OFF permanece pendiente. Se renderizó con la sustitución local disponible de Times New Roman, por lo que conviene comprobar de nuevo el número de páginas al completar autores en Word.
