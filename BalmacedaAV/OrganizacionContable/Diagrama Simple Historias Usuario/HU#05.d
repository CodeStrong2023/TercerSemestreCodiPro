Iniciar
|
|___ El empleado accede al sistema
|       |
|       |___ ¿Es la primera vez que el empleado entra?
|       |       |
|       |       |___ Sí
|       |       |       |
|       |       |       |___ El empleado ingresa su dirección de email y contraseña
|       |       |               |
|       |       |               |___ ¿Los datos son correctos?
|       |       |                       |
|       |       |                       |___ Sí
|       |       |                       |       |
|       |       |                       |       |___ El sistema solicita al empleado ingresar una nueva contraseña
|       |       |                       |               |
|       |       |                       |               |___ El empleado ingresa una nueva contraseña
|       |       |                       |                       |
|       |       |                       |                       |___ ¿La contraseña cumple con los requisitos?
|       |       |                       |                               |
|       |       |                       |                               |___ Sí
|       |       |                       |                               |       |
|       |       |                       |                               |       |___ La nueva contraseña se registra en la base de datos
|       |       |                       |                               |       |
|       |       |                       |                               |       |___ Redirigir al empleado a la página principal
|       |       |                       |                               |
|       |       |                       |                               |___ No
|       |       |                       |                                       |
|       |       |                       |                                       |___ Se muestra un mensaje de error y se vuelve al inicio del proceso
|       |       |                       |
|       |       |                       |___ No
|       |       |                               |
|       |       |                               |___ El empleado ingresa su dirección de email y contraseña
|       |       |                                       |
|       |       |                                       |___ ¿Los datos son correctos?
|       |       |                                               |
|       |       |                                               |___ Sí
|       |       |                                               |       |
|       |       |                                               |       |___ Redirigir al empleado a la página principal
|       |       |
|       |       |___ No
|       |               |
|       |               |___ Se muestra un mensaje de error y se vuelve al inicio del proceso
|       |
|       |___ La sesión del empleado se mantiene activa durante el horario de atención del local
|       |
|       |___ ¿La sesión del empleado está fuera del horario de atención del local?
|               |
|               |___ Sí
|                       |
|                       |___ ¿Ha habido actividad en la sesión en los últimos 30 minutos?
|                               |
|                               |___ Sí
|                               |       |
|                               |       |___ La sesión permanece abierta
|                               |
|                               |___ No
|                                       |
|                                       |___ La sesión se cierra automáticamente
|
|___ Finalizar
