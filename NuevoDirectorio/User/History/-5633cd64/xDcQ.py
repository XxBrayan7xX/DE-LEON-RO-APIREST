import psycopg2
from psycopg2 import pool
from logger_base import log
class conexion:
    _DATABASE = "clase_db" 
    _USERNAME = "postgres"
    _PASSWORD = "Admin123"
    _PORT = "5432"
    _HOST =  "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool =  None
    @classmethod
    def ObtenerPool(cls):
        if cls._pool == None:
            cls._pool=pool.SimpleConnectionPool(I
                cls._MIN_CON,
                cls._MAX_CON,
                host =  cls._HOST,
                user = cls._USERNAME,
                password = cls._PASSWORD,
                port = cls._PORT,
                database = cls._DATABASE
            )
            log.debug("Creacion del pool", pool)
            return cls._pool
        else:
            return cls._pool
        
    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerConexion().getconnO()
        log.debug(f"Conexion obtenida {conexion}")
        return conexion
    @classmethod
    def LiberarConexion(cls, conexion):
        cls.ObtenerPool().puttcon(conexion)
        log.debug(f"Conexion regresada {conexion}")

    @classmethod