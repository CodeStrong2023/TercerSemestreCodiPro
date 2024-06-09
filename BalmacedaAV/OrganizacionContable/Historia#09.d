+-------------------+
|    Administrador  |
+-------------------+
| - id: int         |
| - nombre: String  |
| - apellido: String|
| - email: String   |
+-------------------+

+-------------------+
|    Cliente        |
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
| - productos: Producto[]|
+-------------------+

+-------------------+
|    Sistema        |
+-------------------+
| + buscarProductosPorCategoria(categoria: String): Producto[] |
| + buscarProductosPorNombre(nombre: String): Producto[] |
| + agregarProductoAlCarrito(cliente: Cliente, producto: Producto): void |
+-------------------+

