
import psycopg2  # esto es para poder conectar a Postgre

conexion = psycopg2.connect(
    user='postgres',  # poner usuario correspondiente
    password='admin',  # poner contraseña correspondiente
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
# print(conexion)  # prueba
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # Placeholder
            id_persona = input('Digite un número para el id_persona: ')
            cursor.execute(sentencia, (id_persona,))  # de esta manera ejecutamos la sentencia
            registros = cursor.fetchone()  # recuperamos todos los registros que serán una lista
            print(registros)

# cursor.close()
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# https://www.psycopg.org/docs/usage.html