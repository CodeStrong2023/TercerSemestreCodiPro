import psycopg2 as bd #Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_bd')
try:
    # conexion.autocommit = False #Esto directamente no deberia estar, es una mala practica
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido,email) VALUES (%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparrza@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() #Hacemos el commit manualmente, es una buena practica 
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()