import psycopg2
from logger_base import log

conexion = psycopg2.connect(
    user="postrges",
    password="Admin123",
    host="127.0.0.1",
    port="5432",
    database = "clase_db"
)
try:
    with conexion:
        whit conexion.cursor() as cursor:
            sentencia = "INSERT INTO cliente(id_cliente, nombre) VALUES(%,)"
            valores = (
                ["9","Paco"],
                ["10", "Hugo"],
                ["11","Pedro"]
            )
        cursor.executemany(sentencia,valores)
        registrosInsertados = cursor.rowcount
        log.debug