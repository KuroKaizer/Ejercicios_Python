import psycopg2 as db

conexion = db.connect(user='postgres',
                 password='kakaroto23',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s'
entrada = input("Proporciona la pk a elminar: ")
valores = (entrada,)
#valores = (9,)
cursor.execute(sentencia, valores)
#Guardar la informacion en la base de datos
conexion.commit()
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

cursor.close()
conexion.close()