+-------------------+
|    Cocinero       |
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
| - tiempoEntregaEstimado: int |
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
| + obtenerPedidosAPreparar(): Pedido[] |
| + asignarEstadoPedido(pedido: Pedido, nuevoEstado: String): void |
+-------------------+
