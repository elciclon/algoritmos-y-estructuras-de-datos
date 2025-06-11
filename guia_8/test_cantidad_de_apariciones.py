import unittest

from cantidad_de_apariciones import *


class cantidad_de_aparicionesTest(unittest.TestCase):
    def test_cantidad_de_apariciones(self):
        self.assertEqual(cantidad_de_apariciones("archivo.txt", "perro"), 3)
        self.assertEqual(cantidad_de_apariciones("archivo.txt", "gato"), 2)
        self.assertEqual(cantidad_de_apariciones("archivo.txt", "omnibus"), 1)
        self.assertEqual(cantidad_de_apariciones("archivo.txt", "bolsa"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
