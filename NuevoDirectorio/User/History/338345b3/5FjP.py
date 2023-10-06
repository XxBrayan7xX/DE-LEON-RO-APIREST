from logger_base import log

class Venta:
    def __init__(self,id_venta=None,cantidad=None,total=None) -> None:
        self._id_venta = id_venta
        self._cantidad = cantidad
        self._total = total
    def __str__(self) -> str:
        return f"""
    ID PERSONA: {self._id_venta}, NOMBRE: {self._cantidad}, TOTAL: {self._total}
"""
    @property
    def idVenta(self):
        return self._id_venta
    
    @idVenta.setter
    def idVenta(self):
        return self._id_venta
    
if __name__=="main":
    venta1 = Venta(4,250.5)
    log.debug(venta1)
    venta3=Venta(id_venta = 3)
