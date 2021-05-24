import psycopg2 as db

conexion = db.connect(user='postgres',
                      password='kakaroto23',
                      host='127.0.0.1',
                      port='5432',
                      database='test_db')

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = (
    ('Marcos', 'Cantu', 'Mcantu@mail.com'),
    ('Esteban', 'Hernandez', 'Ehernandez@mail.com'),
    ('Jenni', 'Gonzales', 'Jgonzales@mail.com')
)
cursor.executemany(sentencia, valores)
# Guardar la informacion en la base de datos
conexion.commit()
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()
