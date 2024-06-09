+-------------------+
|      Cajero       |
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
| - formaPago: String |
| - pagoRealizado: boolean |
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
| + asignarEstadoPedido(pedido: Pedido, nuevoEstado: String): void |
| + verificarEstadoPago(pedido: Pedido): boolean |
| + realizarEntrega(pedido: Pedido): void |
+-------------------+
