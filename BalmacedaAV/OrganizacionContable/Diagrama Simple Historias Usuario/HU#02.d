Iniciar
|
|___ El cliente accede al formulario de login desde la barra de navegación
|       |
|       |___ Se presenta al cliente la opción de login con Google o el formulario de login estándar
|               |
|               |___ El cliente ingresa su dirección de email y contraseña en el formulario de login estándar
|                       |
|                       |___ ¿Los datos ingresados son correctos?
|                               |
|                               |___ No
|                                       |
|                                       |___ Se muestra un mensaje de error indicando que los datos son incorrectos y se permite al cliente intentarlo de nuevo
|                               |
|                               |___ Sí
|                                       |
|                                       |___ ¿El cliente está dado de baja?
|                                               |
|                                               |___ Sí
|                                                       |
|                                                       |___ Se muestra un mensaje indicando que el cliente está dado de baja y no puede acceder al sistema
|                                                       |
|                                                       |___ Fin del proceso
|                                               |
|                                               |___ No
|                                                       |
|                                                       |___ El sistema redirige al cliente a la página principal
|                                                               |
|                                                               |___ En la barra de navegación se muestra el nombre del cliente y un menú desplegable con opciones de ver su perfil, historial de pedidos y desconectarse
|                                                                       |
|                                                                       |___ ¿Hay actividad del cliente en el sistema?
|                                                                               |
|                                                                               |___ No
|                                                                                       |
|                                                                                       |___ ¿El tiempo de inactividad supera los 45 minutos?
|                                                                                               |
|                                                                                               |___ Sí
|                                                                                                       |
|                                                                                                       |___ El sistema desconecta automáticamente al cliente y muestra un mensaje indicando que debe iniciar sesión nuevamente
|                                                                                               |
|                                                                                               |___ No
|                                                                                                       |
|                                                                                                       |___ Fin del proceso
|                                                                               |
|                                                                               |___ Sí
|                                                                                       |
|                                                                                       |___ Fin del proceso
|
|___ Finalizar
