import unittest

from factory import Factory


class TestFactory(unittest.TestCase):

    def test_creaAyer(self):
        f = Factory('02/1/2019')
        self.assertIsInstance(f,Factory)

    def test_creaHoy(self):
        f = Factory('29/11/2019')
        print (f.hace_cuántos_días())
        print (f.hoy)

if __name__ == '__main__':
    unittest.main()
