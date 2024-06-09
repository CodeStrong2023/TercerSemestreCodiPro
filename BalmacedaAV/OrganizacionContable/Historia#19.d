+-------------------+
|  Administrador    |
|      - id: int    |
|      - nombre: String |
|      - apellido: String |
|      - email: String |
+-------------------+
        |
        v
+-------------------+
|     Cajero        |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - apellido: String |
|      - email: String |
+-------------------+
         |
         v
+-------------------+
|    NotaCredito    |
+-------------------+
|      - id: int    |
|      - facturaAnulada: Factura |
|      - fechaEmision: Date |
+-------------------+

+-------------------+
|    Factura        |
+-------------------+
|      - id: int    |
|      - pedido: Pedido  |
|      - fecha: Date |
+-------------------+

+-------------------+
|    Pedido         |
+-------------------+
|      - id: int    |
|      - cliente: Cliente |
|      - fecha: Date |
|      - estado: String |
|      - items: Item[] |
+-------------------+

+-------------------+
|    Item           |
+-------------------+
|      - id: int    |
|      - producto: Producto |
|      - cantidad: int |
+-------------------+

+-------------------+
|    Producto       |
+-------------------+
|      - id: int    |
|      - nombre: String |
|      - stock: int |
+-------------------+
