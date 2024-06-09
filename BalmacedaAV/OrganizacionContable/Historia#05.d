+---------------------------------+
|            Empleado             |
+---------------------------------+
| - id: String                    |
| - nombre: String                |
| - email: String                 |
| - contraseña: String            |
| - primeraVez: Boolean           |
| - activo: Boolean               |
+---------------------------------+
| + ingresar(email: String,       |
|    contraseña: String): Boolean |
| + cambiarContraseña(nuevaContraseña: String): Void |
+---------------------------------+

+---------------------------------+
|          Administrador          |
+---------------------------------+
| - id: String                    |
| - nombre: String                |
| - email: String                 |
| - contraseña: String            |
+---------------------------------+
| + registrarEmpleado(email: String, |
|    contraseña: String): Void    |
| + darDeBajaEmpleado(id: String): Void |
+---------------------------------+

+---------------------------------+
|       SistemaAutenticacion      |
+---------------------------------+
| - baseDeDatos: BaseDeDatos      |
+---------------------------------+
| + verificarCredenciales(email: String, |
|    contraseña: String): Boolean |
| + pedirCambioContraseña(empleado: Empleado): Void |
| + iniciarSesion(email: String,   |
|    contraseña: String): Void    |
+---------------------------------+

+---------------------------------+
|           BaseDeDatos           |
+---------------------------------+
| - empleados: List<Empleado>     |
+---------------------------------+
| + buscarEmpleadoPorEmail(email: String): Empleado |
| + guardarEmpleado(empleado: Empleado): Void |
+---------------------------------+

+---------------------------------+
|        FormularioLogin          |
+---------------------------------+
| - email: String                 |
| - contraseña: String            |
+---------------------------------+
| + mostrarFormulario(): Void     |
| + obtenerDatos(): String[]      |
+---------------------------------+

+---------------------------------+
|             Sesion              |
+---------------------------------+
| - empleado: Empleado            |
| - horaInicio: Date              |
| - activa: Boolean               |
+---------------------------------+
| + cerrarSesion(): Void          |
| + verificarInactividad(): Void  |
+---------------------------------+

+---------------------------------+
|         PaginaPrincipal         |
+---------------------------------+
| - nombreEmpleado: String        |
| - menuOpciones: String[]        |
+---------------------------------+
| + mostrarPagina(): Void         |
+---------------------------------+
