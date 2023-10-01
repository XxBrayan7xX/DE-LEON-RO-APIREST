import psycopg2
conexion = psycopg2.connect("user='postgres' password='Admin123' host='127.0.0.1' port='5432' dbname='Puesto'")
print(conexion)
cursor=conexion.cursor()
cursor.execute("SELECT * FROM venta")
resultado = cursor.fetchall()
print(resultado)