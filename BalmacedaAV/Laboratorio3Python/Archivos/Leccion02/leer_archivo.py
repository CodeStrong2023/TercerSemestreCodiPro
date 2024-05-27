
#archivo = open('prueba.txt', 'r', encoding='utf8') # las letras son: 'r' read, 'a' append, 'w' write, 'x' create file
archivo = open('c:\\Users\\AdrianaBalmaceda\\2024semestre3\\TercerSemestreCodiPro\\BalmacedaAV\\Laboratorio3Python\\Archivos\Leccion02\prueba.txt',
               'r', encoding='utf8')
# print(archivo.read())
# print(archivo.read(16)) #(15) probar y ejecutar
# print(archivo.read(10)) #(8)(5) probar y ejecutar #continuamos desde la linea anterior
# print(archivo.readline())
# print(archivo.readline())

# 1-vamos a iterar el archivo, cada una de las lineas
# for linea in archivo:
    # print(linea) #prueba1 iteramos todos los elementos del archivo
# print(archivo.readlines()) # prueba2 accedemos al archivo como si fuera una lista
# print(archivo.readlines(1)) # prueba3
# print(archivo.readlines()[1]) # prueba4
# print(archivo.readlines()[3]) # prueba5
# print(archivo.readlines()[11]) # prueba6

# Anexamos información, copiamos a otro
# archivo2 = open('copia.txt', 'a', encoding='utf8') #caso A
archivo2 = open('copia.txt', 'w', encoding='utf8') #caso B
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')