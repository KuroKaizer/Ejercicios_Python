from logger_base import logger
from psycopg2 import pool
import sys


class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'kakaroto23'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE)
                logger.debug(f'Creacion de Pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.error(f'Error al crear Pool de conexion: {e}')
                sys.exit()
        else:
            return cls.__pool

    # Obtener una conexion del pool
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del Pool: {conexion}')
        return conexion

    # Regredar el objeto conexion al pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexion al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')
    
    # Cerrar el pool y todas las conexiones    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__pool}')            


if __name__ == '__main__':
    # Obtener una conexion a partir del pool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    # Regresar las conexiones al pool
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    # Cerramos el pool
    Conexion.cerrarConexiones()
    # Si intentamos perdir conexion a un pool cerrado
    # conexion1 = Conexion.obtenerConexion()
