+--------------------------------+
|             Cliente            |
+--------------------------------+
| - nombre: String               |
| - direccion: String            |
| - correo: String               |
| - contraseña: String           |
+--------------------------------+
| + verPerfil(): void            |
| + modificarDatos(): void       |
+--------------------------------+
            |
            |
            V
+--------------------------------+
|             Perfil             |
+--------------------------------+
| - datosPersonales: String      |
+--------------------------------+
| + mostrarDatos(): void         |
| + redirigirFormulario(): void  |
+--------------------------------+
            |
            |
            V
+--------------------------------+
|           Formulario           |
+--------------------------------+
| - direccion: String            |
| - nuevaContraseña: String      |
| - confirmarContraseña: String  |
+--------------------------------+
| + cambiarDireccion(): void     |
| + cambiarContraseña(): void    |
| + verificarContraseña(): bool  |
+--------------------------------+
            |
            |
            V
+--------------------------------+
|            Sistema             |
+--------------------------------+
| - baseDeDatos: Map             |
+--------------------------------+
| + validarDatos(): bool         |
| + encriptarContraseña(): String|
| + actualizarDatos(): void      |
| + mostrarMensaje(): void       |
+--------------------------------+
