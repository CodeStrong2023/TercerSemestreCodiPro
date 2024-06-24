from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1= Cuadrado(5, 'Azul')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado : {cuadrado1.Calcular_area()}')

#MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(2,8, "verde")
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)