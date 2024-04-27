from Cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo el area del cuadrado:  {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)

rectangulo = Rectangulo(3, 8, 'verde')
print(f'Calculo del area del rectangulo: {rectangulo.calcular_area()}')
print(rectangulo)