import unittest
from queue import LifoQueue as Pila

from cantidad_elementos import *


class Test_cantidad_elementos(unittest.TestCase):

    def test_cantidad_elementos(self):
        p: Pila = Pila()
        for numero in [3, 56, 6, 8]:
            p.put(numero)
        self.assertEqual(cantidad_elementos(p), 4)

    def test_cantidad_elementos_chars(self):
        p: Pila = Pila()
        for letra in ["a", "b", "c"]:
            p.put(letra)
        self.assertEqual(cantidad_elementos(p), 3)
