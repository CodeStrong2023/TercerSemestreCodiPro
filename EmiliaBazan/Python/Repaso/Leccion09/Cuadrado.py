from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # Llamar al constructor de FiguraGeometrica
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)  # Llamar al constructor de Color

    def CalcularArea(self):
        return self._ancho * self._alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
