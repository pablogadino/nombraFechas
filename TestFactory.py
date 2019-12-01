import unittest

from factory import Factory


class TestFactory(unittest.TestCase):

    def test_creaAyer(self):
        f = Factory()
        self.assertIsInstance(f,Factory)

    def test_creaHoy(self):
        f = Factory()
        f.set_fecha_entrega('1/12/2019')
        print (f.hace_cuántos_días())
        print (f.fecha_entrega)
        día=f.generar()
        print (día.apelativo)

    def test_creaAyer(self):
        f = Factory()
        f.set_fecha_entrega('30/11/2019')
        print (f.hace_cuántos_días())
        print (f.fecha_entrega)
        día = f.generar()
        print (día.apelativo)

if __name__ == '__main__':
    unittest.main()
