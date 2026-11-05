# KiCad: especificación del temporizador NE555

Este caso aparece en la conversación «Recuperar prompt temporizador NE555» como un **prompt reconstruido**, no como transcripción literal del prompt original. Se conserva como caso experimental propuesto y no como resultado ejecutado.

## Objetivo y criterios

Diseñar con KiCad MCP un monoestable NE555 alimentado a 5 V. Una pulsación breve debe encender un LED durante aproximadamente 11 s y permitir un nuevo disparo tras apagarse. La referencia de tiempo es `T = 1,1 × 100 kΩ × 100 µF ≈ 11 s`.

Componentes especificados: NE555 DIP-8; R1 100 kΩ, R2 10 kΩ, R3 330 Ω; C1 100 µF, C2 10 nF, C3 100 nF; LED, pulsador normalmente abierto y conector de alimentación.

Conexiones requeridas: pin 1 a GND; pin 2 con pull-up R2 a 5 V y pulsador a GND; pin 3 a R3 y LED hacia GND; pin 4 a 5 V; pin 5 a C2 hacia GND; pines 6 y 7 al nodo R1–C1; pin 8 a 5 V. R1 conecta 5 V con el nodo de temporización; C1 conecta ese nodo con GND; C3 desacopla 5 V y GND cerca del integrado.

El prompt reconstruido también pedía esquema, PCB de aproximadamente 55 × 40 mm y dos capas, ERC, DRC, vista 3D cuando fuera posible y registro de tiempos, llamadas, errores y correcciones. Esos entregables son **criterios solicitados**; aquí no hay `.kicad_sch`, `.kicad_pcb`, reportes ERC/DRC ni logs originales que demuestren su ejecución.

Para incorporar el caso a los resultados, conservar el prompt realmente enviado, versión de KiCad/MCP, configuración de LM Studio, registros de llamadas y tiempo, archivos de proyecto y reportes de verificación. No calcular porcentajes de completitud ni atribuir una causa de fallo sin esos datos.
