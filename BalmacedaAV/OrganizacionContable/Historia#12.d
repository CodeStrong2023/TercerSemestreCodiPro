+-------------------+
|      Cliente      |
+-------------------+
| - id: int         |
| - nombre: String  |
| - apellido: String|
| - email: String   |
| - direccion: String |
| - telefono: String |
+-------------------+

+-------------------+
|    Pedido         |
+-------------------+
| - id: int         |
| - cliente: Cliente|
| - estado: String  |
| - formaEntrega: String |
| - formaPago: String |
| - direccionEntrega: String |
| - telefonoEntrega: String |
| - items: Item[]   |
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
| - precio: double  |
| - disponible: boolean |
+-------------------+

+-------------------+
|    Sistema        |
+-------------------+
| + confirmarPedido(cliente: Cliente, items: Item[], formaEntrega: String, formaPago: String): void |
+-------------------+
