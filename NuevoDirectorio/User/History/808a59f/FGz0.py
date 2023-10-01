conexion = psycopg2.connect(
    user="Postrges"

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