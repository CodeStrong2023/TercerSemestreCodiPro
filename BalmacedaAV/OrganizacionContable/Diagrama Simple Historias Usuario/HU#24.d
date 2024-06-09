Iniciar
|
|___ ¿Usuario es Cocinero o Administrador? ___
|        |
|        |___ Sí
|        |       |
|        |       |___ Acceder a la página de Control de Stock
|        |
|        |___ No
|                |
|                |___ Mostrar mensaje de acceso denegado
|
|___ Mostrar lista de ingredientes
|       |
|       |___ ¿Stock actual < Stock mínimo?
|               |
|               |___ Sí
|               |       |
|               |       |___ Mostrar ingrediente en la lista de bajos de stock
|               |
|               |___ No
|                       |
|                       |___ ¿Stock actual < 20% del stock mínimo?
|                               |
|                               |___ Sí
|                               |       |
|                               |       |___ Mostrar ingrediente en la lista de cerca del stock mínimo
|                               |
|                               |___ No
|                                       |
|                                       |___ Pasar al siguiente ingrediente
|
|___ Mostrar botón para registrar compra para cada ingrediente en la lista
|       |
|       |___ ¿Se hace clic en el botón de registrar compra?
|               |
|               |___ Sí
|                       |
|                       |___ Redirigir al formulario de registro de compra (HU#23)
|
|___ Finalizar
