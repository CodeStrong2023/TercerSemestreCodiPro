       +------------------+
       |   <<Actor>>      |
       |     Cliente      |
       +------------------+
             |    |
             |    |
        -----+----+------------------------------
             |    |
             v    v
    +---------------------+     +--------------------+
    |Acceder al sistema   |     |Autenticarse con    |
    |                     |<--> |Google              |
    +---------------------+     +--------------------+
             |
             v
    +---------------------+
    |Ingresar credenciales|
    +---------------------+
             |
             v
    +---------------------+
    |Verificar credenciales|
    +---------------------+
             |
             v
    +---------------------+
    |Redirigir a página   |
    |principal            |
    +---------------------+
             |
             v
    +---------------------+
    |Mostrar opciones de  |
    |perfil               |
    +---------------------+
             |
             v
    +---------------------+
    |Desconectar por      |
    |inactividad          |
    +---------------------+
+----------------------+
|       Cliente        |
+----------------------+
| - nombre: String     |
| - email: String      |
| - contraseña: String |
| - estado: String     |
+----------------------+
| + iniciarSesion()    |
| + cerrarSesion()     |
+----------------------+
             |
             |
             v
+----------------------+
|       Sistema        |
+----------------------+
| - usuarios: List     |
+----------------------+
| + verificarCred()    |
| + redirigirPrincipal()|
+----------------------+
             |
             |
             v
+----------------------+
|   FormularioLogin    |
+----------------------+
| - email: String      |
| - contraseña: String |
+----------------------+
| + mostrar()          |
| + verificar()        |
+----------------------+
             |
             |
             v
+----------------------+
|      BaseDatos       |
+----------------------+
| - datosUsuario: List |
+----------------------+
| + obtenerUsuario()   |
| + validarUsuario()   |
+----------------------+
             |
             |
             v
+----------------------+
|      Navegación      |
+----------------------+
| - barra: String      |
+----------------------+
| + mostrarMenu()      |
+----------------------+
