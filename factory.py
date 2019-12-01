from datetime import datetime
from Ayer import Ayer
from Hoy import Hoy


class Factory:

    def __init__(self, str_fecha):
        self.str_fecha = str_fecha
        self.fecha_y_hora_entrega = datetime.strptime(str_fecha, '%d/%m/%Y')
        self.fecha_entrega=self.fecha_y_hora_entrega.date()

        self.ahora = datetime.now()
        self.str_ahora = "% s / % s / % s " % (self.ahora.day, self.ahora.month, self.ahora.year)

        self.hoy = self.ahora.date()

    def generar(self):
        if(self.fecha==self.hoy):
            return Hoy(self.fecha)
        if(self.hace_cuántos_días()==1)
            return Ayer(self.fecha)
        if (self.hace_cuántos_días() == 1)
            return Ayer(self.fecha)

    def hace_cuántos_días(self):
        delta = self.fecha_entrega - self.hoy
        return (delta.days)