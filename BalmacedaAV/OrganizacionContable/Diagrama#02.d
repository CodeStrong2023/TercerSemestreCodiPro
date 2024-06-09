Inicio
|
|---[1. Acceder al formulario de login]--- ¿Cliente?
|                                          |
|                                          Sí
|                                          |
|                                          No
|                                          |
|                                          Fin
|
|---[2. Loguearse con Google]-------------- ¿Loguearse con Google?
|                                          |
|                                          Sí
|                                          |
|                                          No
|                                          |
|                                          Fin
|
|---[3. Completar formulario de login]---- ¿Datos ingresados correctamente?
|    |                                     |
|    Sí                                    No
|    |                                     |
|    |---[3.1 Verificar en la base de datos]--- ¿Datos válidos?
|         |                                   |
|         Sí                                  No
|         |                                   |
|         |---[3.2 Mostrar error]------------ Mostrar mensaje de error y permitir nuevo intento
|                                             |
|---[4. Redirigir al cliente a la página principal]--- Redirigir al cliente a la página principal
