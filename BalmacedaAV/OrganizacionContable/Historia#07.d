+------------------+
|   Administrador  |
+------------------+
| - id: int        |
| - nombre: String |
| - apellido: String|
| - email: String  |
+------------------+
| + verListadoClientes(): void |
| + modificarCliente(cliente: Cliente): void |
| + darAltaBajaCliente(cliente: Cliente): void |
+------------------+

+------------------+
|      Cliente     |
+------------------+
| - id: int        |
| - nombre: String |
| - apellido: String|
| - direccion: String |
| - telefono: String |
| - email: String  |
+------------------+

+------------------------+
|   Sistema              |
+------------------------+
| + buscarCliente(id: int): Cliente |
| + guardarCambiosCliente(cliente: Cliente): void |
| + cambiarEstadoCliente(cliente: Cliente): void |
+------------------------+
