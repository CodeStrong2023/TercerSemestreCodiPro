from FiguraGeometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        color.__init__(self, color)

    def Calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"
