import unittest

from factory import Factory


class TestFactory(unittest.TestCase):

    def test_creaAyer(self):
        f = Factory('02/1/2019')
        self.assertIsInstance(f,Factory)
        print (f.fecha.date())
        print (f.ahora.date())



if __name__ == '__main__':
    unittest.main()
