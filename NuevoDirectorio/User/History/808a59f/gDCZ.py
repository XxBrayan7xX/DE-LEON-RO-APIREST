import psycopg2
from logger_base import log

conexion = psycopg2.connect("user='postrges' password='Admin123' host='127.0.0.1' port='5432' database = 'Puesto'")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO venta(id_cliente, nombre) VALUES(%S,)"
            valores = (
                ("9", "250.0"),
                ("7", "200.0"),
                ("3", "105.5")
            )
        cursor.executemany(sentencia,valores)
        registrosInsertados = cursor.rowcount
        log.debug
except Exception as e:
    log.error(e)
    print(e)
finally:
    conexion.close()