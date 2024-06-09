+------------------+
|  Administrador   |
+------------------+
| - id: int        |
| - nombre: String |
| - apellido: String|
| - email: String  |
+------------------+
| + registrarEmpleado() |
+------------------+

                1
                |
                |
                |
                *
+------------------+
|   Empleado       |
+------------------+
| - id: int        |
| - nombre: String |
| - apellido: String|
| - direccion: String |
| - departamento: String |
| - telefono: String |
| - email: String  |
| - clave: String  |
| - rol: Rol       |
+------------------+
| + modificarClave() |
+------------------+

                1
                |
                |
                |
                *
+------------------+
|      Rol         |
+------------------+
| - id: int        |
| - nombre: String |
+------------------+

+---------------------+
| RegistroEmpleadoForm|
+---------------------+
| - nombre: String    |
| - apellido: String  |
| - direccion: String |
| - departamento: String|
| - telefono: String  |
| - email: String     |
| - clave: String     |
| - claveConfirm: String |
| - rol: Rol          |
+---------------------+
| + validarEmail(): Boolean  |
| + validarClave(): Boolean  |
| + validarConfirmacionClave(): Boolean |
| + verificarEmailUnico(): Boolean |
+---------------------+

+------------------------+
|   Sistema              |
+------------------------+
| + verificarEmail(): Boolean |
| + verificarClave(): Boolean |
| + verificarEmailUnico(): Boolean |
| + registrarEmpleado(): void |
+------------------------+
