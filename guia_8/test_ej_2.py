import unittest
from queue import LifoQueue as Pila

from cantidad_elementos import *
from buscar_nota_maxima import *


def pila_a_lista(p: Pila) -> list:
    aux: list = []
    temp: list = []

    while not p.empty():
        elem = p.get()
        aux.append(elem)
        temp.append(elem)

    for elemento in reversed(temp):
        p.put(elemento)
    return aux


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


class Test_buscar_nota_maxima(unittest.TestCase):
    def test_buscar_nota_maxima_un_elemento(self):
        p: Pila = Pila()
        p.put(("a", 10))
        antes: list = pila_a_lista(p)
        self.assertEqual(buscar_nota_maxima(p), ("a", 10))
        despues: list = pila_a_lista(p)
        self.assertEqual(antes, despues)

    def test_buscar_nota_maxima_varios_elementos(self):
        p: Pila = Pila()
        for alumno in [("a", 5), ("b", 10), ("c", 7), ("d", 0)]:
            p.put(alumno)
        antes: list = pila_a_lista(p)
        self.assertEqual(buscar_nota_maxima(p), ("b", 10))
        despues: list = pila_a_lista(p)
        self.assertEqual(antes, despues)
