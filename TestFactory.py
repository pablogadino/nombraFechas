import unittest

from factory import Factory


class TestFactory(unittest.TestCase):

    def test_crea_factory(self):
        f = Factory()
        self.assertIsInstance(f,Factory)

    def test_crea_hoy(self):
        f = Factory()
        f.fecha_comparada='1/12/2019'
        día=f.generar()
        print (día)

    def test_crea_ayer(self):
        f = Factory()
        f.fecha_comparada='30/11/2019'
        día = f.generar()
        print (día)

    def test_crea_anteyer(self):
        f = Factory()
        f.fecha_comparada = '29/11/2019'
        día = f.generar()
        print(día)

    def test_crea_día_antiguo(self):
        f = Factory()
        f.fecha_comparada = '2/11/2019'
        día = f.generar()
        print(día)

if __name__ == '__main__':
    unittest.main()
