class NumerosIgualesException (Exception): #extiende de la clase
    def __init__(self, mensaje):
        self.message = mensaje