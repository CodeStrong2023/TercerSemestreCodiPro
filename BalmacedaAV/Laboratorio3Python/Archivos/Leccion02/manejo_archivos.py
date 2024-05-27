# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #la w es de write = escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n') #encoding='utf8'(tildes)
    archivo.write('las letras son: \nr read leer, \na append anexar, \nw write escribir, \nx crear un archivo')
    archivo.write('\nt esta es text texto, \nb archivos binarios, \nw+ lee y escribe, son iguales r+\n')
    archivo.write('Saludos a todos mis compañeros de la Tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
#archivo.write('Todo quedó perfecto') #este es un error