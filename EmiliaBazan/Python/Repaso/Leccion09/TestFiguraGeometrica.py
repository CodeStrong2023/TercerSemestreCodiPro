import Cuadrado

cuadrado1 = Cuadrado.Cuadrado(3, 'Azul')

print(cuadrado1._ancho)
print(cuadrado1._alto)
print(f'Calulo del area de un cuadrado: {cuadrado1.CalcularArea()}')


# MRO: Method Resolution Order (Permite conocer las jerarquías de las clases frente a la clase actual)

print(Cuadrado.Cuadrado.mro())
