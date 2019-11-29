import unittest

from Ayer import Ayer


class TestAyer(unittest.TestCase):

    def test_crea(self):
        nuevo = Ayer('s')
        self.assertIsInstance(nuevo, Ayer)

    def test_nombra(self):
        nuevo = Ayer('2/09/2019')
        self.assertEqual(nuevo.nombrar(), 'ayer')


if __name__ == '__main__':
    unittest.main()
