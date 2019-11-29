from datetime import datetime
from Ayer import Ayer


class Factory:

    def __init__(self, str_fecha):
        self.str_fecha = str_fecha
        self.fecha = datetime.strptime(str_fecha, '%d/%m/%Y')

        self.ahora = datetime.datetime.now()
        self.ahora_string = "% s / % s / % s " % (self.ahora.day, self.ahora.month, self.ahora.year)

    def generar(self):
        return Ayer(self.fecha)

