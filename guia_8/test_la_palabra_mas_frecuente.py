import unittest

from la_palabra_mas_frecuente import *


class la_palabra_mas_frecuenteTest(unittest.TestCase):
    def test_la_palabra_mas_frecuente(self):
        self.assertEqual(la_palabra_mas_frecuente("archivo.txt"), "perro")


if __name__ == "__main__":
    unittest.main(verbosity=2)
