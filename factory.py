from datetime import datetime
from Anteayer import Anteayer
from Ayer import Ayer
from Hoy import Hoy
from Día import Día
class FactoryDíaError(Exception):
    pass
class Factory:

    def __init__(self):
        self.ahora = datetime.now()
        self.str_ahora = "% s / % s / % s " % (self.ahora.day, self.ahora.month, self.ahora.year)
        self.hoy = self.ahora.date()
        self.str_hoy =self.str_ahora

    def set_fecha_entrega(self,str_fecha):
        self.str_fecha_entrega = str_fecha
        self.fecha_y_hora_entrega = datetime.strptime(str_fecha, '%d/%m/%Y')
        self.fecha_entrega=self.fecha_y_hora_entrega.date()

    def generar(self):
        if(self.fecha_entrega == self.hoy):
            return Hoy(self.fecha_entrega )
        if(self.hace_cuántos_días()==1):
            return Ayer(self.fecha_entrega)
        if (self.hace_cuántos_días() == 2):
            return Anteayer(self.fecha_entrega)
        if (self.hace_cuántos_días() > 2):
            return Día(self.fecha_entrega)
        raise FactoryDíaError

    def hace_cuántos_días(self):
        delta = self.hoy - self.fecha_entrega
        return (delta.days)