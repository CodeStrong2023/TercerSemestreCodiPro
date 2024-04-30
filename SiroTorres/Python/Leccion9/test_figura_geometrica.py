from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul')
cuadrado1.alto = 7
#cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f'Calculo el area del cuadrado:  {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)
print('Creacion de objeto clase Rectangulo'.center(50, '_'))
rectangulo = Rectangulo(3, 9, 'verde')
rectangulo.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo.calcular_area()}')
print(rectangulo)

# figura1 = FiguraGeometrica() No se puede instanciar, es abstracta
print(Cuadrado.mro())