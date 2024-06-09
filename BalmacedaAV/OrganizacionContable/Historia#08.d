+------------------+
|   Administrador  |
+------------------+
| - id: int        |
| - nombre: String |
| - apellido: String|
| - email: String  |
+------------------+
| + verListadoEmpleados(): void |
| + modificarEmpleado(empleado: Empleado): void |
| + darAltaBajaEmpleado(empleado: Empleado): void |
| + verRolesDisponibles(): Rol[] |
| + asignarNuevoRol(empleado: Empleado, nuevoRol: Rol): void |
+------------------+

+------------------+
|      Empleado     |
+------------------+
| - id: int        |
| - nombre: String |
| - apellido: String|
| - direccion: String |
| - departamento: String |
| - telefono: String |
| - email: String  |
| - rol: Rol       |
+------------------+

+------------------+
|        Rol       |
+------------------+
| - id: int        |
| - nombre: String |
+------------------+

+------------------------+
|   Sistema              |
+------------------------+
| + buscarEmpleado(id: int): Empleado |
| + guardarCambiosEmpleado(empleado: Empleado): void |
| + cambiarEstadoEmpleado(empleado: Empleado): void |
+------------------------+
