import pyscopg2
conexion = pyscopg2.connect("user='postgres' password = 'Admin123' host = '127.0.0.1' port = '5432' dbname =  'Puesto'")
print(conexion)
cursor=conexion.cursor()
cursor.execute("SELECT * FROM ventas")
resultado = cursor.fetchall()
print(resultado)