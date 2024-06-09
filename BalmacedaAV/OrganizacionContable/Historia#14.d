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
| + obtenerPedidosPorEstado(estado: String): Pedido[] |
| + buscarPedidoPorId(id: int): Pedido |
+-------------------+
