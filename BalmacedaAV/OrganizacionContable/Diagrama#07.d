Inicio
|
|---[1. Acceder al listado de clientes]--- ¿El administrador desea acceder al listado de clientes?
|                                         |
|                                         Sí
|                                         |
|                                         No
|                                         |
|                                         Fin
|
|---[2. Mostrar listado de clientes]--------- Mostrar listado de clientes con datos y botón de modificación
|
|---[3. Seleccionar cliente para modificar]-- ¿El administrador selecciona un cliente para modificar?
|                                           |
|                                           Sí
|                                           |
|                                           No
|                                           |
|                                           Fin
|
|---[4. Redirigir al formulario de modificación]--- Redirigir al formulario de modificación del cliente seleccionado
|
|---[5. Modificar datos del cliente]------------ Modificar los datos del cliente (excepto la contraseña)
|
|---[6. Guardar cambios]------------------------ ¿El administrador desea guardar los cambios?
|    |                                         |
|    Sí                                        No
|    |                                         |
|    |---[6.1 Actualizar datos del cliente]---- Actualizar datos del cliente en la base de datos
|    |                                         |
|    No                                        |
|    |                                         |
|    |---[6.2 Cancelar modificación]----------- Cancelar la modificación y volver al listado de clientes
|
|---[7. Dar de alta/baja al cliente]------------ ¿El administrador desea dar de alta/baja al cliente?
|    |                                         |
|    Sí                                        No
|    |                                         |
|    |---[7.1 Guardar cambios]----------------- Actualizar estado del cliente en la base de datos
|    |                                         |
|    No                                        |
|    |                                         |
|    |---[7.2 Cancelar modificación]----------- Cancelar la modificación y volver al listado de clientes
|
|---[8. Finalizar]------------------------------ Fin
