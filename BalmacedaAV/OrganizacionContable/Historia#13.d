+-------------------+
|      Cliente      |
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
| - numeroPedido: String |
| - total: double   |
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
|    Factura        |
+-------------------+
| - id: int         |
| - pedido: Pedido  |
| - fecha: Date     |
| - subtotal: double|
| - descuento: double |
| - total: double   |
+-------------------+

+-------------------+
|    Sistema        |
+-------------------+
| + obtenerPedidos(cliente: Cliente): Pedido[] |
| + obtenerDetallePedido(pedido: Pedido): Item[] |
| + obtenerFactura(pedido: Pedido): Factura |
+-------------------+
