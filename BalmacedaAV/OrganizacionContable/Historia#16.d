+-------------------+
|     Delivery      |
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
| - formaEntrega: String |
| - direccionEntrega: String |
| - telefonoEntrega: String |
+-------------------+

+-------------------+
|       Item        |
+-------------------+
| - id: int         |
| - producto: Producto|
| - cantidad: int   |
+-------------------+

+-------------------+
|    Sistema        |
+-------------------+
| + obtenerPedidosEnDelivery(): Pedido[] |
| + asignarEstadoPedido(pedido: Pedido, nuevoEstado: String): void |
+-------------------+
