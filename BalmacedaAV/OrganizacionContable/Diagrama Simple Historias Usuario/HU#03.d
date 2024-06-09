Iniciar
|
|___ El cliente accede a la opción de ver su perfil
|       |
|       |___ Se redirige al cliente a una página donde puede ver sus datos personales
|               |
|               |___ El cliente hace clic en el botón para modificar sus datos
|                       |
|                       |___ Se redirige al cliente a un formulario de modificación de datos
|                               |
|                               |___ El cliente modifica sus datos personales y/o contraseña
|                                       |
|                                       |___ ¿La nueva contraseña cumple con los criterios de seguridad?
|                                               |
|                                               |___ No
|                                                       |
|                                                       |___ Se muestra un mensaje de error indicando que la contraseña no cumple con los criterios de seguridad y se vuelve al formulario
|                                               |
|                                               |___ Sí
|                                                       |
|                                                       |___ ¿Las contraseñas coinciden?
|                                                               |
|                                                               |___ No
|                                                                       |
|                                                                       |___ Se muestra un mensaje de error indicando que las contraseñas no coinciden y se vuelve al formulario
|                                                               |
|                                                               |___ Sí
|                                                                       |
|                                                                       |___ Se actualizan los datos del cliente en la base de datos del sistema
|                                                                               |
|                                                                               |___ Fin del proceso
|
|___ Finalizar
