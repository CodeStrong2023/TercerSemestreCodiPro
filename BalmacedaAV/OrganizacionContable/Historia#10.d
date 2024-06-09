+-------------------+
|      Cliente      |
+-------------------+
|      - id: int    |
|      - nombre: String |
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
|      - precio: double |
+-------------------+

+-------------------+
|    Sistema        |
+-------------------+
| + buscarProducto(palabraClave: String): List<Producto> |
+-------------------+
