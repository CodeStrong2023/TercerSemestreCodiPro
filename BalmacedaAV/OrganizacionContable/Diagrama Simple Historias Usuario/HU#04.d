Iniciar
|
|___ El administrador accede al formulario de registro de nuevo empleado
|       |
|       |___ El administrador ingresa los datos del nuevo empleado (nombre, apellido, dirección, departamento, teléfono, email y contraseña provisoria)
|               |
|               |___ ¿Los datos son válidos?
|                       |
|                       |___ No
|                               |
|                               |___ Se muestra un mensaje de error indicando los datos incorrectos y se vuelve al inicio del proceso
|                       |
|                       |___ Sí
|                               |
|                               |___ El administrador selecciona el rol del nuevo empleado
|                               |
|                               |___ El administrador confirma la contraseña ingresada
|                                       |
|                                       |___ ¿Las contraseñas coinciden?
|                                               |
|                                               |___ No
|                                                       |
|                                                       |___ Se muestra un mensaje de error indicando que las contraseñas no coinciden y se vuelve al inicio del proceso
|                                               |
|                                               |___ Sí
|                                                       |
|                                                       |___ ¿La dirección de email es válida?
|                                                               |
|                                                               |___ No
|                                                                       |
|                                                                       |___ Se muestra un mensaje de error indicando que la dirección de email es inválida y se vuelve al inicio del proceso
|                                                               |
|                                                               |___ Sí
|                                                                       |
|                                                                       |___ ¿Ya existe un empleado registrado con el mismo email?
|                                                                               |
|                                                                               |___ Sí
|                                                                                       |
|                                                                                       |___ Se muestra un mensaje de error indicando que ya existe un empleado con ese email y se vuelve al inicio del proceso
|                                                                               |
|                                                                               |___ No
|                                                                                       |
|                                                                                       |___ Se registra al nuevo empleado en la base de datos de la empresa con la contraseña encriptada
|                                                                                               |
|                                                                                               |___ Fin del proceso
|
|___ Finalizar
