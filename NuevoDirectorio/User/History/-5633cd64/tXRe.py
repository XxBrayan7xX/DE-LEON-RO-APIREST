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
            cls._MIN_CON