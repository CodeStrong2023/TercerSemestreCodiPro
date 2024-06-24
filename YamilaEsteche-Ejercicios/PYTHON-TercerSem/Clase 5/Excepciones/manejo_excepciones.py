from NumerosIgualesException import NumerosIgualesException
resultado = None
a = 10
b = 2
try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}')
else:
    print('No se arrojo ninguna excepción')
finally: # siempre se va a ejecutar finally
    print('Ejecución de este bloque finally')

print(f'El resultado es: {resultado}')
print('seguimos...')
