+-------------------+
|  Administrador    |
+-------------------+
| - id: int         |
| - nombre: String  |
| - apellido: String|
| - email: String   |
+-------------------+

+-------------------+
|    Pedido         |
+-------------------+
| - id: int         |
| - cliente: Cliente|
| - fecha: Date     |
| - estado: String  |
| - items: Item[]   |
| - total: float    |
+-------------------+

+-------------------+
|    Factura        |
+-------------------+
| - id: int         |
| - pedido: Pedido  |
| - fecha: Date     |
+-------------------+

+-------------------+
|    Cliente        |
+-------------------+
| - id: int         |
| - nombre: String  |
| - apellido: String|
| - email: String   |
| - direccion: String|
+-------------------+

+-------------------+
|       Item        |
+-------------------+
| - id: int         |
| - producto: Producto|
| - cantidad: int   |
+-------------------+

+-------------------+
|    Producto       |
+-------------------+
| - id: int         |
| - nombre: String  |
| - precio: float   |
+-------------------+

+-------------------+
|    Sistema        |
+-------------------+
| + generarFactura(pedido: Pedido): void |
+-------------------+
