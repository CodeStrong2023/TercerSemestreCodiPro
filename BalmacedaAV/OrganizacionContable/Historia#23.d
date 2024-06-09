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
|      - precioCosto: double |
|      - stock: int |
|      - unidadMedida: String |
|      - activo: boolean |
+-------------------+

+-------------------+
|    RegistroCompra |
+-------------------+
|      - id: int    |
|      - ingrediente: Ingrediente |
|      - precioCosto: double |
|      - cantidad: int |
|      - fechaCompra: Date |
+-------------------+

+-------------------+
|      Sistema      |
+-------------------+
| + registrarCompra(ingredienteId: int, precioCosto: double, cantidad: int): void |
+-------------------+
