import unittest
from nivel_de_ocupacion import *

class Nivel_de_ocupacionTest(unittest.TestCase):
    def test_nivel_de_ocupacion(self):
        self.assertEqual(nivel_de_ocupacion([[True, False, False], [False,False,True], [True, True, True]]), [2/3, 1/3, 1.0])

if __name__ == "__main__":
    unittest.main(verbosity = 2)