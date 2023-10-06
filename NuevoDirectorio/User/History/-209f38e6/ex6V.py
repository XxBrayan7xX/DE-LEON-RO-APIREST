import psycopg2
from EjerciciosNoExpo.Semana2.logger_base import log
conexion=psycopg2.connect("user='postgres' password='Admin123' host='127.0.0.1' port='5432' dbname='Puesto'")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia="DELETE FROM venta where id_venta in %s"
            entrada=input("ID's A Eliminar ")
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registrosEliminados=cursor.rowcount
            log.debug(f"registros eliminados: {registrosEliminados}")
except Exception as e:
    log.error(e)
    print(e)
finally:
    conexion.close()