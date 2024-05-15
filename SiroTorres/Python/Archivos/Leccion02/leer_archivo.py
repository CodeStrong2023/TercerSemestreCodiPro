
archivo = open('prueba.txt', 'r', encoding='utf8') #Las letras son: 'r'read, 'a'append, 'w'wrrite, 'x'
# print(archivo.read())
#print(archivo.read(16))
#print(archivo.read(10)) #Continuamos desde la linea anterior
#print(archivo.readline())
#print(archivo.readline())

# Vamos a iterra el archivo, cada una de las lineas
# for linea in archivo:
    # print(linea): iteramos todos los elementos del archivo
# print(archivo.readlines()[11]) # accedemos al archivo como si fuera una lista

# Anexamos informacio, copiamos a otro
archivo2 = open('copia.txt', s'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() #Cerrramos el primer archivo
archivo2.close() #Cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')

