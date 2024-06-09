Inicio
|
|---[1. Acceder al formulario de login]---- ¿Es la primera vez que el empleado entra?
|                                         |
|                                         Sí
|                                         |
|                                         No
|                                         |
|                                         Fin
|
|---[2. Mostrar formulario de login]-------- Mostrar formulario con campos para dirección de email y contraseña
|
|---[3. Ingresar datos del empleado]-------- Ingresar dirección de email y contraseña
|
|---[4. Verificar datos del empleado]------- ¿Datos correctos?
|    |                                      |
|    Sí                                     No
|    |                                      |
|    |---[4.1 Mostrar error]---------------- Mostrar mensaje de error y permitir intentarlo de nuevo
|    |                                      |
|    No                                     |
|    |                                      |
|    |---[5. Es la primera vez?]------------ Sí
|    |    |                                 |
|    |    |                                 Sí
|    |    |                                 |
|    |    |                                 No
|    |    |                                 |
|    |    |---[5.1 Mostrar formulario]------ No
|    |    |                                 |
|    |    |---[5.2 Redirigir a la página principal]--- Fin
|    |    |
|    |    No
|    |    |
|    |    |---[6. Redirigir a la página principal]--- Fin
|    |
|---[7. Cierre de sesión]-------------------- Fin
