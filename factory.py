from datetime import datetime
from Ayer import Ayer


class Factory:

    def __init__(self, str_fecha):
        self.str_fecha = str_fecha
        self.fecha = datetime.strptime(str_fecha, '%d/%m/%Y').date()

        self.ahora = datetime.now()
        self.str_ahora = "% s / % s / % s " % (self.ahora.day, self.ahora.month, self.ahora.year)

        self.hoy = self.ahora.date()

    def generar(self):
        if(self.fecha==self.hoy):
            return Hoy(self.fecha)

