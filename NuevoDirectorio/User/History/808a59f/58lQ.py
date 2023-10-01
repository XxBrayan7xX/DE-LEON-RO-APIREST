import psycopg2
from logger_base import log

conexion = psycopg2.connect("user='postgres' password='Admin123' host='127.0.0.1' port='5432' dbname='Puesto'")
print(conexion)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO venta (cantidad, total) VALUES (%s,%s)"
            valores = (
                ("9", "250.0"),
                ("7", "200.0"),
                ("3", "105.5")
            )
        cursor.executemany(sentencia,valores)
        registrosInsertados = cursor.rowcount
        log.debug(f"Registros insertdos: {registrosInsertados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()