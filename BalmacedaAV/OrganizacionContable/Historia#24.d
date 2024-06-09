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
|     Ingrediente    |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - stockMinimo: int |
|      - stockActual: int |
|      - unidadMedida: String |
+-------------------+

+-------------------+
|   ControlStock    |
+-------------------+
| + mostrarIngredientesBajosStock(): List<Ingrediente> |
| + mostrarIngredientesCercaStockMinimo(porcentaje: double): List<Ingrediente> |
+-------------------+
