from NumerosIgualesException import NumerosIgualesException

resultado = None #prueba2
#a = 7 #10  #'10' #prueba3
#b = 0 #5 #0

try:
    a = int(input('Digite el primer número: ')) #prueba5
    b = int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    #10/0 #prueba1
    resultado = a / b #prueba2 modificamos
except TypeError as e: #prueba4
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e: #prueba1 #prueba3 #prueba4
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else: #prueba6
    print("No se arrojo ninguna excepción")
finally: #prueba7 siempre se va a ejecutar
    print("Ejecución de este bloque finally")

print(f'El resultado es : {resultado}') #prueba2
print('seguimos...')
