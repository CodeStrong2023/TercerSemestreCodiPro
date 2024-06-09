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
|      RubroProducto|
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - activo: boolean |
+-------------------+

+-------------------+
|      Sistema      |
+-------------------+
| + obtenerRubrosProducto(): RubroProducto[] |
| + crearRubroProducto(nombre: String, activo: boolean): void |
| + modificarRubroProducto(rubro: RubroProducto): void |
| + eliminarRubroProducto(rubro: RubroProducto): void |
+-------------------+
