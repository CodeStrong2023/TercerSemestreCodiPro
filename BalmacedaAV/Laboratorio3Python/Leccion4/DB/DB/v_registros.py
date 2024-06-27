import psycopg2  # esto es para poder conectar a Postgre

conexion = psycopg2.connect(
    user='postgres',  # poner usuario correspondiente
    password='admin',  # poner contraseña correspondiente
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2)'  # Placeholder
            entrada = input('Digite los id_persona(separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            # id_persona = input('Digite un número para el id_persona: ')
            cursor.execute(sentencia, llaves_primarias)  # de esta manera ejecutamos la sentencia
            registros = cursor.fetchall()  # recuperamos todos los registros que serán una lista
            for registro in registros:
                print(registro)

# cursor.close()
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# https://www.psycopg.org/docs/usage.html