import psycopg2 as db

conexion = db.connect(user = 'postgres',
                 password = 'kakaroto23',
                 host = '127.0.0.1',
                 port = '5432',
                 database = 'test_db')

try:
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Marcos', 'Tunez', 'Mtunez@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Mathias', 'Saavedra', 'Msaavedra@mail.com', 10)
    cursor.execute(sentencia, valores)

    #Guardar la informacion en la base de datos
    conexion.commit()
except Exception as e:
    #rollback para dar maracha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f'Ocurrio un error en la transiccion: {e}')    
finally:
    cursor.close()
    conexion.close()