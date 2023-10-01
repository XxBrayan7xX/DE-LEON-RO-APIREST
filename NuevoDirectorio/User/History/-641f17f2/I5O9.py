import psycopg2
from logger_base import log
conexion = psycopg2.connect("user='postgres' password='Admin123' host='127.0.0.1' port='5432' dbname='Puesto'")
try:
    conexion.autocommit=False
    cursor=conexion.cursor()
    sentencia="INSERT INTO Venta (id_venta, cantidad, total) values(%s,%s,%s)"
    valores=("5", "150.0")
    cursor.execute(sentencia,valores)
    log.debug("sentencia  INSERT")
    conexion.commit()
    update = "UPDATE Venta SET cantidad %s where id_venta = %s"
    valores = ("4", "1")
    log.debug("sentencia UPDATE")
except Exception as e:
    conexion.rollback()
    log.error(e)

