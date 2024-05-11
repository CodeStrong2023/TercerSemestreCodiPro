from NumerosigualesException import NumerosigualesException
resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    if a == b:
        raise NumerosigualesException('Son numeros iguales')
    resultado = a / b #modificamos
except TypeError as e:
    print(f'TypeError - Ocurrrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrrio un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}')
else:
    print("No se arrojo ninguna excepcion ")
finally: #Siempre se va a ejecutar
    print("Ejecucion de este bloque finally")

print(f'El resultado es: {resultado}')
print('seguimos...')