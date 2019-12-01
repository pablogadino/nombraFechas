from datetime import datetime


class Día:

    apelativo = 'el'

    def __init__(self, str_fecha: str):
        self.__str_fecha = str_fecha

    @property
    def número_día_con_mes(self):
        return self.__str_fecha[:-5]

    def nombrar(self):
        return self.apelativo

    def __str__(self):
        return self.apelativo + ' ' + self.número_día_con_mes


