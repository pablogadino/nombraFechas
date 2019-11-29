import unittest

from factory import Factory


class TestFactory(unittest.TestCase):

    def test_creaAyer(self):
        f = Factory('2019/11/2')
        self.assertIsInstance(Factory, f)



if __name__ == '__main__':
    unittest.main()
