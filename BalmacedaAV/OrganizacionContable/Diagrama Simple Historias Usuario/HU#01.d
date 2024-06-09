Iniciar
|
|___ El cliente accede al formulario de registro desde la barra de navegación
|       |
|       |___ Se presenta al cliente la opción de registro con Google o el formulario de registro estándar
|               |
|               |___ El cliente completa el formulario de registro estándar ingresando sus datos personales y contraseña
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
|                                                       |___ Se muestra un mensaje indicando que el cliente está dado de baja y no puede registrarse nuevamente
|                                                       |
|                                                       |___ Fin del proceso
|                                               |
|                                               |___ No
|                                                       |
|                                                       |___ ¿El cliente ya está registrado con la misma dirección de email?
|                                                               |
|                                                               |___ Sí
|                                                                       |
|                                                                       |___ Se muestra un mensaje indicando que ya existe un cliente registrado con la misma dirección de email y se permite al cliente intentarlo de nuevo
|                                                               |
|                                                               |___ No
|                                                                       |
|                                                                       |___ ¿Las contraseñas coinciden?
|                                                                               |
|                                                                               |___ No
|                                                                                       |
|                                                                                       |___ Se muestra un mensaje indicando que las contraseñas no coinciden y se permite al cliente intentarlo de nuevo
|                                                                               |
|                                                                               |___ Sí
|                                                                                       |
|                                                                                       |___ Los datos son registrados en la base de datos del sistema, con la contraseña encriptada
|                                                                                       |
|                                                                                       |___ El sistema asigna automáticamente el rol de cliente al nuevo registro
|                                                                                       |
|                                                                                       |___ Se redirige al cliente a la página principal, apareciendo en la barra de navegación su nombre y un menú desplegable con opciones de ver su perfil, historial de compras y desconectarse
|
|___ Finalizar
