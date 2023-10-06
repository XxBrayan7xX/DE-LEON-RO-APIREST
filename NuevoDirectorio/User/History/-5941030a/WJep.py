from Persona import Venta
from conexion import conexion
from cursorDelPool import CursorDelPool
from logger_base import log

class PersonDAO:
    _SELECCIONAR = "SELECT FROM venta ORDER BY id_venta"
    _INSERTAR = "INSERT INTO venta(canatidad, total) VALUES(%s,%s)"
    _ACTUALIZAR = "UPDATE venta SET canatidad=%s"
    _ELIMINAR = "DELET From venta where id_venta = %s"

@classmethod
def seleccionar(cls):
    with CursorDelPool() as cursor:
        cursor.execute(cls._SELECCIONAR)
        registro=cursor.fetchall()
        personas = []
        for r in registros:
            personas.append(Persona(r[0],r[1],r[2],r[3])) 
        return personas
@classmethod
def insertar(cls,persona):
    with CursorDelPool as cursor:
        valores = (persona.Nombre, persona.Apellido, persona.correo, )
        cursor.execute(cls._INSERTAR, valores)
        return cursor.rowcount
    
@classmethod
def actualizar(cls,persona):
    with CursorDelPool as cursor:
        valores = (persona.Nombre, persona.Apellido, persona.correo, )
        cursor.execute(cls._ACTUALIZAR, valores)
        return cursor.rowcount

@classmethod
def eliminar(cls,persona):
    with CursorDelPool as cursor:
        valores = (persona.id_persona,)
        cursor.execute(cls._ELIMINAR, valores)
        return cursor.rowcount
if __name__ == "__main__":
    persona1 =  Persona(nombre="Diego", apellidoo= "Perez", email="dpere.gmail.com")
    Insercion = 