#01 Este diagrama de flujo describe el proceso de registro de un nuevo cliente en el sistema. 
Comienza cuando el cliente accede al formulario de registro desde la barra de navegación. 
Luego, el cliente completa el formulario de registro ingresando sus datos personales y contraseña. 
Si los datos ingresados son incorrectos, se muestra un mensaje de error y se permite al cliente intentarlo de nuevo. 
Si los datos son correctos, se verifica si el cliente está dado de baja. 
Si lo está, se muestra un mensaje indicando que no puede registrarse nuevamente. 
Si no lo está, se verifica si el cliente ya está registrado con la misma dirección de email. 
Si lo está, se muestra un mensaje indicando que ya existe un cliente registrado con la misma dirección de email 
y se permite al cliente intentarlo de nuevo. Si no lo está, se verifica si las contraseñas coinciden. 
Si no lo hacen, se muestra un mensaje indicando que las contraseñas no coinciden y se permite al cliente intentarlo de nuevo. 
Si lo hacen, los datos son registrados en la base de datos del sistema, con la contraseña encriptada, 
y se asigna automáticamente el rol de cliente al nuevo registro. 
Finalmente, se redirige al cliente a la página principal y aparece su nombre en la barra de navegación 
junto con un menú desplegable de opciones.

#02 Este diagrama de flujo describe el proceso de ingreso al sistema como cliente. 
Comienza cuando el cliente accede al formulario de login desde la barra de navegación. 
Luego, el cliente ingresa sus credenciales de acceso. 
Si los datos ingresados son incorrectos, se muestra un mensaje de error y se permite al cliente intentarlo de nuevo.
Si los datos son correctos, se verifica si el cliente está dado de baja. 
Si lo está, se muestra un mensaje indicando que no puede acceder al sistema. 
Si no lo está, el sistema redirige al cliente a la página principal y muestra su nombre en la barra de navegación. 
Luego, se verifica si hay actividad del cliente en el sistema. 
Si no la hay y el tiempo de inactividad supera los 45 minutos, el sistema desconecta automáticamente al cliente 
y muestra un mensaje indicando que debe iniciar sesión nuevamente. 
Si hay actividad del cliente o el tiempo de inactividad no supera los 45 minutos, el proceso finaliza.

#03 Este diagrama de flujo describe el proceso de actualización de datos por parte de un cliente. 
Comienza cuando el cliente accede a la opción de ver su perfil, desde donde puede ver sus datos personales. 
Luego, el cliente decide modificar sus datos y/o contraseña, lo que lo lleva a un formulario de modificación.
 Después de realizar los cambios, se verifica si la nueva contraseña cumple con los criterios de seguridad establecidos. 
 Si la contraseña no cumple con los criterios, se muestra un mensaje de error y se vuelve al formulario. 
 Si cumple con los criterios, se verifica si las contraseñas coinciden. 
 Si las contraseñas no coinciden, se muestra un mensaje de error y se vuelve al formulario. 
 Si las contraseñas coinciden, se actualizan los datos del cliente en la base de datos del sistema. 
 Si en algún momento se detecta un error, se muestra un mensaje correspondiente y se vuelve al formulario.

#04 Este diagrama de flujo describe el proceso de registro de un nuevo empleado por parte del administrador. 
Comienza con el administrador ingresando los datos del nuevo empleado en el formulario de registro. 
Luego, se verifica la validez de los datos ingresados, incluida la coincidencia de las contraseñas, 
la validez del correo electrónico y si ya existe un empleado registrado con el mismo correo electrónico. 
Si todos los criterios son cumplidos, se registra al nuevo empleado en la base de datos de la empresa con la contraseña encriptada. 
Si en algún punto del proceso se detecta un error, se muestra un mensaje de error correspondiente y se vuelve al inicio del proceso.

#05 Este diagrama de flujo describe el proceso de ingreso al sistema para un empleado. 
Comienza con la verificación de si es la primera vez que el empleado ingresa al sistema. 
Luego, se verifica la validez de los datos ingresados. 
Si es la primera vez, se solicita al empleado que ingrese una nueva contraseña y se comprueba si cumple con los requisitos. 
Si no es la primera vez, se verifica la validez de los datos ingresados. 
Si los datos son correctos, se redirige al empleado a la página principal. 
La sesión del empleado se mantiene activa durante el horario de atención del local y se cierra automáticamente 
si está fuera de ese horario y no ha habido actividad en la sesión en los últimos 30 minutos.

#06 Este diagrama de flujo describe el proceso de actualización de datos por parte de un empleado. 
Comienza con el acceso del empleado a la opción de ver su perfil, donde puede visualizar sus datos personales. 
Si decide modificar sus datos, se le redirige a un formulario donde puede ingresar los nuevos datos. 
Después de validar los datos ingresados, se actualizan en la base de datos si son válidos, de lo contrario se muestra un mensaje de error.

#07 Este diagrama de flujo describe el proceso de modificación y baja de clientes por parte del administrador. 
Comienza con el acceso al listado de clientes, donde el administrador puede ver los datos de cada cliente y decide si desea modificar alguno. 
En caso afirmativo, se muestra un formulario de modificación donde el administrador puede actualizar los datos (excepto la contraseña) y, 
opcionalmente, dar de alta/baja al cliente. Si decide dar de alta/baja, se actualiza el estado de activación del cliente. 
Si no desea modificar ningún cliente, el flujo finaliza.

#08 Este diagrama de flujo describe el proceso de modificación y baja de empleados por parte del administrador. 
Comienza con el acceso al listado de empleados, donde el administrador puede ver los datos de cada empleado y decide si desea modificar alguno. 
En caso afirmativo, se muestra un formulario de modificación donde el administrador puede actualizar los datos (excepto la contraseña) y, 
opcionalmente, dar de alta/baja al empleado. Si decide dar de alta/baja, se actualiza el estado de activación del empleado. 
Si no desea modificar ningún empleado, el flujo finaliza.

#09 Este diagrama de flujo describe el proceso de interacción en la página principal para clientes. 
Comienza mostrando la página principal con la barra de navegación, el cuadro de búsqueda y los productos disponibles. 
Dependiendo de si el cliente está logueado o no, se muestran los botones correspondientes. 
Se permite al cliente ver el detalle de un producto y agregar productos al carrito. 
Finalmente, se muestra el carrito de compras a la derecha de la página.

#10 Este diagrama describe el flujo de interacciones que ocurren cuando un cliente realiza una búsqueda de productos. 
Comienza con el cliente ingresando una búsqueda en el cuadro de búsqueda. 
Luego, se verifica si la búsqueda devuelve resultados o no. 
Si hay resultados, se muestran al cliente; de lo contrario, se le informa que no se encontraron resultados. 
Si el cliente no ingresa una búsqueda, permanece en la página principal.

#11 Este diagrama describe el flujo de interacciones que ocurren cuando un cliente utiliza el carrito de compras. 
Comienza con la adición de un producto al carrito, donde se verifica si el producto ya está presente en el carrito o no. 
Luego, el cliente puede decidir eliminar un producto del carrito o modificar la cantidad de un producto. 
Finalmente, el cliente puede confirmar el pedido y proceder al proceso de opciones de entrega y pago, 
o puede continuar comprando o realizar otras acciones en la página principal.

#12 Este diagrama describe el proceso de confirmación del pedido para un cliente. 
Comienza con la verificación de si el cliente ha iniciado sesión en el sistema. 
Si ha iniciado sesión, se le pregunta al cliente si desea confirmar el pedido. 
Luego, se le ofrece la opción de elegir entre retiro en local o envío a domicilio, con la correspondiente acción de aplicar 
un descuento del 10% en caso de retiro en local. 
Después, se presenta la selección de la forma de pago, según las opciones disponibles en función de la elección anterior. 
Finalmente, el pedido se confirma y se llevan a cabo las acciones necesarias según la opción de pago elegida. 
Si el cliente no ha iniciado sesión, se lo redirige a la pantalla de inicio de sesión.

#13 Este diagrama describe el proceso para que un cliente vea su historial de pedidos. 
Comienza con el cliente iniciando sesión en el sistema. 
Si el inicio de sesión es exitoso, se muestra el historial de pedidos. 
Luego, el cliente puede seleccionar un pedido para ver su detalle. 
Desde el detalle del pedido, el cliente puede optar por visualizar la factura, y se le ofrecen opciones para imprimir o descargar la factura. 
Una vez que se realiza la acción deseada o el cliente decide no realizarla, el proceso finaliza.

#14 Este diagrama describe el proceso de vista y recepción de pedidos por parte del cajero. 
Comienza con el acceso a la página de pedidos, donde se muestra una grilla con todos los pedidos y su información. 
Luego, el cajero puede filtrar los pedidos por estado o buscar un pedido específico por su ID. 
Una vez realizada la selección o búsqueda, el proceso finaliza.

#15 Este diagrama describe el proceso de administración de estado, cobro y entrega de pedidos por parte del cajero. 
Comienza con la revisión de los pedidos "A confirmar". 
Si el pedido está correcto, se asigna el estado "A cocina" si hay ítems que requieren preparación, o el estado "Listo" si no hay ítems 
que necesiten pasar por cocina. 
Luego, se verifica si hay pedidos en estado "Listo". 
Si los hay, se asigna el estado correspondiente según la opción de envío seleccionada por el cliente. 
Si no hay pedidos en estado "Listo", el proceso finaliza.

#16 Este diagrama describe el flujo para que el delivery vea los pedidos en estado "En delivery". 
Comienza con el acceso a la página de pedidos en delivery, donde se muestra una grilla con todos los pedidos en ese estado. 
El delivery puede seleccionar un pedido para ver su detalle, que incluye información como el nombre y apellido del cliente, 
el teléfono y la dirección de entrega. Después de revisar el detalle, el delivery puede marcar el pedido como "Entregado". 
Una vez marcado como "Entregado", el pedido se elimina de la grilla de pedidos en delivery. 
Si no se selecciona un pedido para ver el detalle, el sistema continúa mostrando la grilla de pedidos en delivery. 
El proceso se repite hasta que el delivery finalice la actividad.

#17 Este diagrama describe el flujo para que el cocinero vea y prepare los pedidos. 
Comienza con el acceso a la página de pedidos a preparar, donde se muestra una grilla con todos los pedidos pendientes. 
El cocinero puede seleccionar un pedido para ver su detalle, que incluye los productos pedidos y la receta de cada uno, 
así como el tiempo aproximado de entrega calculado por el sistema. 
Después de revisar el detalle, el cocinero puede marcar el pedido como "Listo" si está preparado. 
Una vez marcado como "Listo", el pedido se elimina de la grilla de pedidos a preparar. 
Si no se selecciona un pedido para ver el detalle, el sistema continúa mostrando la grilla de pedidos a preparar. 
El proceso se repite hasta que el cocinero finalice la actividad.

#18 Este diagrama describe el flujo para la generación automática de facturas. 
Comienza con la verificación de si el pedido está marcado como pagado. 
Si lo está, el sistema procede a emitir automáticamente la factura correspondiente y luego la envía por correo electrónico al cliente. 
Si el pedido no está marcado como pagado, el sistema espera hasta que lo esté y luego continúa con la generación de la factura. 
Una vez completada esta acción, se finaliza el proceso.

#19 Este diagrama describe el flujo para la anulación de una factura mediante la emisión de una nota de crédito. 
Comienza con la pregunta sobre si se necesita anular una factura. 
Si la respuesta es afirmativa, se procede a emitir la nota de crédito, generando una nueva con los mismos ítems e importes que la 
factura original y agregando los ingredientes descontados al stock. 
Una vez completada esta acción, se finaliza el proceso. 
Si la respuesta es negativa, el proceso se finaliza sin realizar ninguna acción.

#20 Este diagrama describe el flujo de la historia de usuario para el alta, modificación y baja de rubros de ingredientes. 
Permite al usuario (cocinero o administrador) acceder a la página de gestión de rubros de ingredientes, donde puede ver una grilla 
con todos los rubros disponibles. Desde esta página, el usuario puede optar por agregar un nuevo rubro, modificar un rubro existente 
o simplemente ver la lista de rubros. 
Si se decide agregar o editar un rubro, se redirige al formulario correspondiente. 
Una vez completado el formulario y confirmado el ingreso o edición del rubro, se actualiza la base de datos con la información del rubro 
y se redirige nuevamente a la grilla de rubros. 
Si se cancela el ingreso o edición del rubro, simplemente se redirige a la grilla de rubros sin realizar cambios.

#21 Este diagrama describe el flujo de la historia de usuario para el alta, modificación y baja de rubros de productos. 
Permite al usuario (cocinero o administrador) acceder a la página de gestión de rubros de productos, donde puede ver una grilla con 
todos los rubros disponibles. Desde esta página, el usuario puede optar por agregar un nuevo rubro, modificar un rubro existente o 
simplemente ver la lista de rubros. 
Si se decide agregar o editar un rubro, se redirige al formulario correspondiente. 
Una vez completado el formulario y confirmado el ingreso o edición del rubro, se actualiza la base de datos con la información del rubro y 
se redirige nuevamente a la grilla de rubros. 
Si se cancela el ingreso o edición del rubro, simplemente se redirige a la grilla de rubros sin realizar cambios.

#22 Este diagrama describe el flujo de la historia de usuario para el alta, modificación y baja de productos. 
Permite al usuario (cocinero o administrador) acceder a la página de gestión de productos, donde puede ver una grilla con todos los productos
disponibles. Desde esta página, el usuario puede optar por agregar un nuevo producto, modificar un producto existente o 
simplemente ver la lista de productos. 
Si se decide agregar o editar un producto, se redirige al formulario correspondiente. 
Una vez completado el formulario y confirmado el ingreso o edición del producto, se valida si se ha ingresado al menos un ingrediente. 
Si es así, se actualiza la base de datos con la información del producto y se redirige nuevamente a la grilla de productos. 
Si no se ha ingresado ningún ingrediente, se muestra un mensaje indicando que se debe agregar al menos uno.

#23 Este diagrama describe el flujo de la historia de usuario para registrar la compra de ingredientes. 
Permite al usuario (cocinero o administrador) acceder al formulario de registro de compra de ingredientes donde puede seleccionar 
un ingrediente de una lista desplegable. Una vez seleccionado el ingrediente, se muestran campos para ingresar el precio de costo y 
la cantidad comprada. 
Si se ingresan estos datos, se actualiza el stock y el precio de costo del ingrediente en la base de datos y se muestra un mensaje de 
compra registrada exitosamente. 
Si no se selecciona un ingrediente, se muestra un mensaje indicando que se debe hacer esta selección.

#24 Este diagrama describe el flujo de la historia de usuario, desde el inicio hasta la finalización. 
Permite al usuario (cocinero o administrador) acceder a la página de control de stock donde se muestran los ingredientes bajos de stock y 
los que están cerca del stock mínimo. Además, muestra un botón para registrar una compra para cada ingrediente en la lista. 
Si el usuario hace clic en el botón para registrar una compra, se redirige al formulario correspondiente para registrar la compra del 
ingrediente seleccionado.

#25 Este diagrama de flujo describe el proceso de visualización y exportación del ranking de productos para el Administrador. 
Comienza cuando el Administrador accede a la página de Ranking de Productos. 
Se muestra un formulario para seleccionar las fechas y luego se muestran dos grillas separadas, una para productos de cocina y 
otra para bebidas, con los productos ordenados por cantidad vendida de mayor a menor. 
Luego, se pregunta si el Administrador desea exportar la información a un archivo Excel. 
Si no lo desea, no se realiza ninguna acción adicional. Si lo desea, se exporta la información y se descarga automáticamente.

#26 Este diagrama de flujo describe el proceso de visualización y exportación del ranking de clientes para el Administrador. 
Comienza cuando el Administrador accede a la página de Ranking de Clientes. 
Se muestra un formulario para seleccionar las fechas de análisis y luego se presenta otro formulario para seleccionar 
el orden de clasificación, ya sea por cantidad de pedidos o importe total. 
Después, se muestran los clientes con la cantidad de pedidos de cada uno y el importe total de todos los pedidos, 
ordenados según la selección del Administrador. También se muestra un botón "Ver Pedidos" para cada cliente. 
Finalmente, se pregunta si el Administrador desea exportar la información a un archivo Excel. 
Si no lo desea, no se realiza ninguna acción adicional. 
Si lo desea, se exporta la información y se descarga automáticamente.

#27 Este diagrama de flujo describe el proceso de visualización y exportación de los movimientos monetarios para el Administrador. 
Comienza cuando el Administrador accede a la página de Movimientos Monetarios. 
Se muestra un formulario para seleccionar las fechas de análisis y luego se presentan los totales de ingresos, costos y ganancias 
del local entre las fechas seleccionadas. También se muestra un botón para exportar la información a un archivo Excel. 
Finalmente, se pregunta si el Administrador desea exportar la información. 
Si no lo desea, no se realiza ninguna acción adicional. 
Si lo desea, se exporta la información y se descarga automáticamente.
