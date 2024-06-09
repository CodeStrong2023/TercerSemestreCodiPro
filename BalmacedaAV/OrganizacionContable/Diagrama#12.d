Inicio
|
|---[1. Verificar sesión]---------------- ¿El cliente ha iniciado sesión?
|    |
|    Sí
|    |
|    |---[2. Verificar tipo de entrega]----- ¿El cliente desea retiro en local o envío a domicilio?
|    |    |
|    |    Retiro en local
|    |    |
|    |    |---[2.1. Ofrecer descuento]-------- Mostrar opción de descuento del 10%
|    |    |
|    |    |---[2.2. Elegir forma de pago]----- Mostrar opciones de pago: Efectivo o Mercado Pago
|    |    |
|    |    |---[2.3. Confirmar pedido]--------- Mostrar resumen del pedido y botón de confirmación
|    |         |
|    |         |---[2.3.1. Pedido confirmado]-- Actualizar el estado del pedido a "A confirmar"
|    |         |
|    |         |---[2.3.2. Actualizar stock]--- Descontar del stock de ingredientes los productos pedidos
|    |         |
|    |         |---[2.3.3. Mostrar tiempo estimado]-- Calcular y mostrar tiempo estimado de entrega
|    |         |
|    |         |---[2.3.4. Generar factura]---- Generar factura y enviarla al cliente por correo electrónico
|    |         |
|    |         |---[2.3.5. Redirigir a detalle de pedido]-- Mostrar detalle del pedido confirmado
|    |    
|    |    Envío a domicilio
|    |    |
|    |    |---[2.1. Pedir dirección y teléfono]-- Solicitar dirección y teléfono del cliente
|    |    |
|    |    |---[2.2. Elegir forma de pago]------- Mostrar opción de pago: Mercado Pago
|    |    |
|    |    |---[2.3. Confirmar pedido]----------- Mostrar resumen del pedido y botón de confirmación
|    |         |
|    |         |---[2.3.1. Pedido confirmado]--- Actualizar el estado del pedido a "A confirmar"
|    |         |
|    |         |---[2.3.2. Actualizar stock]---- Descontar del stock de ingredientes los productos pedidos
|    |         |
|    |         |---[2.3.3. Mostrar tiempo estimado]-- Calcular y mostrar tiempo estimado de entrega
|    |         |
|    |         |---[2.3.4. Generar factura]----- Generar factura y enviarla al cliente por correo electrónico
|    |         |
|    |         |---[2.3.5. Redirigir a detalle de pedido]-- Mostrar detalle del pedido confirmado
|    |
|    No
|    |
|    |---[3. Redirigir a página de inicio de sesión]-- Redirigir al cliente a la página de inicio de sesión
|
Fin
