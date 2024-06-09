Inicio
|
|---[1. Revisar pedidos "A confirmar"]------ El cajero revisa los pedidos con estado "A confirmar"
|    |
|    |---[2. Asignar estado "A cocina" o "Listo"]-- El cajero decide si el pedido debe ir a cocina o está listo
|    |    |
|    |    |---[2.1. Asignar estado "A cocina"]------ Si el pedido necesita preparación, asignar estado "A cocina"
|    |    |
|    |    |---[2.2. Asignar estado "Listo"]-------- Si el pedido no necesita preparación, asignar estado "Listo"
|    |
|    |---[3. Revisar pedidos "Listo"]---------- El cajero revisa los pedidos con estado "Listo"
|    |    |
|    |    |---[3.1. Asignar estado "En delivery" o "Entregado"]-- El cajero decide si el pedido se entrega o envía a domicilio
|    |         |
|    |         |---[3.1.1. Asignar estado "En delivery"]---- Si el cliente eligió envío a domicilio, asignar estado "En delivery"
|    |         |
|    |         |---[3.1.2. Asignar estado "Entregado"]------ Si el cliente eligió retiro en local y ya retiró, asignar estado "Entregado"
|    |
Fin
