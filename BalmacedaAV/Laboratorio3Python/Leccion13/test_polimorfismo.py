from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)   # de manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto)) # esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if(isinstance(objeto, Gerente)):
        print(objeto.departamento)

empleado = Empleado('Armando', 50000)   #empleado: [Nombre: Ariel, Sueldo: 50000]
imprimir_detalles(empleado)

gerente = Gerente('Noelia', 60000, 'Sistemas')  #gerente: Gerente [ Departamento: Sistemas] Empleado: [Nombre: Noelia]
imprimir_detalles(gerente)