Iniciar
|
|___ Revisar pedidos "A confirmar"
|       |
|       |___ ¿El pedido está todo correcto?
|       |       |
|       |       |___ Sí
|       |       |       |
|       |       |       |___ ¿Hay ítems que requieran preparación?
|       |       |       |       |
|       |       |       |       |___ Sí
|       |       |       |       |       |
|       |       |       |       |       |___ Asignar estado "A cocina"
|       |       |       |       |       |___ Finalizar
|       |       |       |       |
|       |       |       |       |___ No
|       |       |       |               |
|       |       |       |               |___ Asignar estado "Listo"
|       |       |       |               |___ Finalizar
|       |       |       |
|       |       |       |___ No
|       |       |               |
|       |       |               |___ Continuar revisando pedidos
|       |
|       |___ Finalizar
|
|___ Cambio de estado de pedidos
|       |
|       |___ ¿Hay pedidos en estado "Listo"?
|       |       |
|       |       |___ Sí
|       |       |       |
|       |       |       |___ ¿El cliente eligió envío a domicilio?
|       |       |       |       |
|       |       |       |       |___ Sí
|       |       |       |       |       |
|       |       |       |       |       |___ Asignar estado "En delivery"
|       |       |       |       |       |___ Finalizar
|       |       |       |       |
|       |       |       |       |___ No
|       |       |       |               |
|       |       |       |               |___ Asignar estado "Entregado" si el cliente retiró el pedido en local
|       |       |       |               |___ Finalizar
|       |       |       |
|       |       |       |___ No
|       |       |               |
|       |       |               |___ Continuar
|       |
|       |___ Finalizar
|
|___ Finalizar
