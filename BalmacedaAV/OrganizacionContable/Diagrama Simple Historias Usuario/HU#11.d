Iniciar
|
|___ ¿El cliente agrega un producto al carrito?
|       |
|       |___ Sí
|       |       |
|       |       |___ ¿El producto ya está en el carrito?
|       |               |
|       |               |___ Sí
|       |               |       |
|       |               |       |___ Actualizar cantidad y subtotal del producto en el carrito
|       |               |
|       |               |___ No
|       |                       |
|       |                       |___ Agregar producto al carrito con cantidad y subtotal
|       |
|       |___ No
|               |
|               |___ ¿El cliente elimina un producto del carrito?
|                       |
|                       |___ Sí
|                       |       |
|                       |       |___ Eliminar producto del carrito y actualizar subtotal general
|                       |
|                       |___ No
|
|___ ¿El cliente desea modificar la cantidad de algún producto en el carrito?
|       |
|       |___ Sí
|       |       |
|       |       |___ Modificar cantidad del producto en el carrito y actualizar subtotal general
|       |
|       |___ No
|
|___ ¿El cliente desea confirmar el pedido?
|       |
|       |___ Sí
|       |       |
|       |       |___ Ir al proceso de opciones de entrega y pago
|       |
|       |___ No
|               |
|               |___ Continuar comprando o realizar otras acciones en la página principal
|
|___ Finalizar
