from ManejoArchivos import ManejoArchivos

#MANEJO DE CONTEXTO WITH : Sintaxis simplificada, abre y cierra el archivo
# with open ('prueba','r',encoding='utf8') as archivo:
   # print(archivo.read())
#No hace falta ni el try ni el family
#en el contexto de with lo que se ejecuta se maneja de forma automatica
#utiliza diferentes metodos __enter este es el que abre
# ahora el siguiente metodo es el que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

