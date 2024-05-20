from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '\n'
        return f'Orden: {self.id_orden}, \nProductos:\n{productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    producto3 = Producto('Top', 100.00)
    producto4 = Producto('Short', 120.00)
    producto5 = Producto('Blusa', 160.00)
    producto6 = Producto('Falda', 180.00)

    productos1 = [producto1, producto3, producto5]
    orden1 = Orden(productos1)
    print(orden1)
    print(f'Total de la orden1: {orden1.calcular_total()}\n')

    productos2 = [producto2, producto4, producto6]
    orden2 = Orden(productos2)
    print(orden2)
    print(f'Total de la orden2: {orden2.calcular_total()}')