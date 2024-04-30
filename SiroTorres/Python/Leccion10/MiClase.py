class MiClase:
    # Variable de clase, este atributo dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia): #La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
miClase = MiClase('Esta es una variable de instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)