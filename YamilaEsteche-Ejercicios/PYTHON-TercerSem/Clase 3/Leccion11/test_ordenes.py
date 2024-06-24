from Orden import Orden
from Producto import Producto
###TEST: CODIGO PROFESOR###
producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Top', 100.00)
producto4 = Producto('Short', 120.00)
producto5 = Producto('Blusa', 160.00)
producto6 = Producto('Falda', 180.00)
productos1 = [producto1, producto2]  # lista de productos
orden1 = Orden(productos1)  # primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto3)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')