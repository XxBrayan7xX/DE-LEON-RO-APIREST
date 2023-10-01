import psycopg2
from logger_base import log
conexion = psycopg2.connect("user='postres' password='Admin123' host='127.0.0.1' port='5432' dbname='Puesto'")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia="UPDATE Venta SET cantidad=%s where id_venta=%s"
            valores=(("5","180.0"))
            cursor.execute(sentencia,valores)
            registrosActualizados=cursor.rowcount
            log.debug(f"registros actualizados {registrosActualizados}")
except Exception as e:
    log.error(e)
    print(e)
finally:
    conexion.close()