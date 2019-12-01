from datetime import datetime
from Anteayer import Anteayer
from Ayer import Ayer
from Hoy import Hoy
from Día import Día
class FactoryDíaError(Exception):
    pass
class Factory:

    def __init__(self):
        self.set_ahora()
        self.str_ahora = "% s / % s / % s " % (self.ahora.day, self.ahora.month, self.ahora.year)
        self.hoy = self.ahora.date()
        self.str_hoy =self.str_ahora

    def set_ahora(self):
        self.ahora = datetime.now()

    def __set_fecha_comparada(self,str_fecha):
        self.__str_fecha_comparada = str_fecha
        self.__fecha_y_hora_comparada = datetime.strptime(str_fecha, '%d/%m/%Y')
        self.__fecha_comparada=self.__fecha_y_hora_comparada.date()

    @property
    def str_fecha_comparada(self):
        return self.__str_fecha_comparada

    @property
    def fecha_comparada(self):
        return self.__fecha_comparada

    @fecha_comparada.setter
    def fecha_comparada(self, valor):
        self.__set_fecha_comparada(valor)

    def generar(self):
        if(self.fecha_comparada == self.hoy):
            return Hoy(self.str_fecha_comparada )
        if(self.hace_cuántos_días()==1):
            return Ayer(self.str_fecha_comparada)
        if (self.hace_cuántos_días() == 2):
            return Anteayer(self.str_fecha_comparada)
        if (self.hace_cuántos_días() > 2):
            return Día(self.str_fecha_comparada)
        raise FactoryDíaError

    def hace_cuántos_días(self):
        delta = self.hoy - self.fecha_comparada
        return (delta.days)