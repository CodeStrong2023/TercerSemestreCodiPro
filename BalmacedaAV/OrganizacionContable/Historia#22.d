+-------------------+
|     Cocinero      |
|   / Administrador |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - apellido: String |
|      - email: String |
+-------------------+
         |
         v
+-------------------+
|      Producto     |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - descripcion: String |
|      - receta: String |
|      - tiempoCocina: int |
|      - rubro: RubroProducto |
|      - imagen: String |
|      - precioVenta: double |
|      - ingredientes: List<Ingrediente> |
|      - activo: boolean |
+-------------------+

+-------------------+
|      RubroProducto|
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - activo: boolean |
+-------------------+

+-------------------+
|     Ingrediente    |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - precioCosto: double |
|      - unidadMedida: String |
|      - activo: boolean |
+-------------------+

+-------------------+
|      Sistema      |
+-------------------+
| + obtenerProductos(): Producto[] |
| + crearProducto(producto: Producto): void |
| + modificarProducto(producto: Producto): void |
| + eliminarProducto(producto: Producto): void |
+-------------------+
