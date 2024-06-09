Inicio
|
|---[1. Acceder al listado de empleados]--- ¿El administrador desea acceder al listado de empleados?
|                                         |
|                                         Sí
|                                         |
|                                         No
|                                         |
|                                         Fin
|
|---[2. Mostrar listado de empleados]--------- Mostrar listado de empleados con datos y botón de modificación
|
|---[3. Seleccionar empleado para modificar]-- ¿El administrador selecciona un empleado para modificar?
|                                           |
|                                           Sí
|                                           |
|                                           No
|                                           |
|                                           Fin
|
|---[4. Redirigir al formulario de modificación]--- Redirigir al formulario de modificación del empleado seleccionado
|
|---[5. Modificar datos del empleado]------------ Modificar los datos del empleado (excepto la contraseña)
|
|---[6. Cambiar rol del empleado]----------------- ¿El administrador desea cambiar el rol del empleado?
|    |                                         |
|    Sí                                        No
|    |                                         |
|    |---[6.1 Seleccionar nuevo rol]----------- Mostrar lista de roles disponibles y seleccionar uno nuevo
|    |                                         |
|    |---[6.2 Guardar cambios]----------------- Actualizar el rol del empleado en la base de datos
|    |                                         |
|    No                                        |
|    |                                         |
|    |---[6.3 Cancelar cambio de rol]---------- Cancelar el cambio de rol y volver al formulario de modificación
|
|---[7. Guardar cambios]------------------------ ¿El administrador desea guardar los cambios?
|    |                                         |
|    Sí                                        No
|    |                                         |
|    |---[7.1 Actualizar datos del empleado]--- Actualizar datos del empleado en la base de datos
|    |                                         |
|    No                                        |
|    |                                         |
|    |---[7.2 Cancelar modificación]----------- Cancelar la modificación y volver al listado de empleados
|
|---[8. Dar de alta/baja al empleado]------------ ¿El administrador desea dar de alta/baja al empleado?
|    |                                         |
|    Sí                                        No
|    |                                         |
|    |---[8.1 Guardar cambios]----------------- Actualizar estado del empleado en la base de datos
|    |                                         |
|    No                                        |
|    |                                         |
|    |---[8.2 Cancelar modificación]----------- Cancelar la modificación y volver al listado de empleados
|
|---[9. Finalizar]------------------------------ Fin
