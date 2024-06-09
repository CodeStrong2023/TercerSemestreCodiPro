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
|      Rubro        |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - activo: boolean |
+-------------------+

+-------------------+
|      Sistema      |
+-------------------+
| + obtenerRubros(): Rubro[] |
| + crearRubro(nombre: String, activo: boolean): void |
| + modificarRubro(rubro: Rubro): void |
| + eliminarRubro(rubro: Rubro): void |
+-------------------+
