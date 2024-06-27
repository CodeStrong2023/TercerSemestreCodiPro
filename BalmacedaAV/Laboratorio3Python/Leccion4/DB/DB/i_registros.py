
import psycopg2  # esto es para poder conectar a Postgre

conexion = psycopg2.connect(
    username='postgres',  # poner usuario correspondiente
    password='admin',  # poner contraseña correspondiente
    host='localhost',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUE(%s, %s, %s)'  # Placeholder
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(sentencia, valores)  # de esta manera ejecutamos la sentencia
            # conexion.commit() # esto se utiliza para guardar los cambios de la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

# cursor.close()
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# https://www.psycopg.org/docs/usage.html