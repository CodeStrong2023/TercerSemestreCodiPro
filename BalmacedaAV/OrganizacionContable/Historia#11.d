+-------------------+
|      Cliente      |
+-------------------+
| - id: int         |
| - nombre: String  |
| - apellido: String|
| - email: String   |
+-------------------+

+-------------------+
|    Producto       |
+-------------------+
| - id: int         |
| - nombre: String  |
| - precio: double  |
| - disponible: boolean |
| - categoria: String |
+-------------------+

+-------------------+
|    Carrito        |
+-------------------+
| - id: int         |
| - cliente: Cliente|
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
| + agregarProductoAlCarrito(cliente: Cliente, producto: Producto, cantidad: int): void |
| + modificarCantidadProductoEnCarrito(cliente: Cliente, producto: Producto, cantidad: int): void |
| + eliminarProductoDelCarrito(cliente: Cliente, producto: Producto): void |
| + calcularSubtotal(item: Item): double |
| + calcularTotal(carrito: Carrito): double |
+-------------------+
