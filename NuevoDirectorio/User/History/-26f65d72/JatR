from logger_base import log
from conexion import conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio bloque with")
        self._conexion = conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_exepcion, valor_exepcion, detalle_exepcion):
        log.debug("Se ejecuta exit")
        if valor_exepcion:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        conexion.LiberarConexion(self._conexion)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("bloque")
        cursor.execute("SELECT * FROM venta")
        log.debug(cursor.fetchall())

        