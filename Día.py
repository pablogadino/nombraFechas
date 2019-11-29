from datetime import datetime

class Día:

    apelativo = 'día'

    def __init__(self, fecha: datetime):
        self.fecha = fecha

    def nombrar(self):
        return self.apelativo


