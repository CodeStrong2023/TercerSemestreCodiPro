class NumerosigualesException (Exception): #Extiende de la clase
    def __init__(self, mensaje):
        self.message = mensaje