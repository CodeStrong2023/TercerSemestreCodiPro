
from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):  #self: Gerente [ Departamento: Sistemas] Empleado: [Nombre: Noelia, Sueldo: 60000]
        return f'Gerente: [Departamento: {self.departamento}], Empleado: [{self.nombre}, Sueldo: {self.sueldo}]'

    #ME DA ERROR
    #    def __str__(self):
        #return f'Gerente [ Departamento: {self.departamento}] {super().__str__()}'

    def mostrar_detalles(self):
        return self.__str__()