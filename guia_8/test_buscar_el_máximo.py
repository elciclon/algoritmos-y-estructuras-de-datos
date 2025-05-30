import unittest
from buscar_el_maximo import *
from queue import LifoQueue as Pila


# Dada una pila, devuelve una lista con los mismos elementos que la pila y sin modificar la pila pasada como parámetro por referencia.
def pila_a_lista(pila: Pila[int]) -> list[int]:
    aux: list[int] = []
    temp: list[int] = []
    while not pila.empty():
        elem = pila.get()
        aux.append(elem)
        temp.append(elem)
    # Restaurar la pila
    for elem in reversed(temp):
        pila.put(elem)
    return aux


class Test_buscar_el_máximo(unittest.TestCase):
    def test_un_solo_elemento(self) -> None:
        pila: Pila[int] = Pila()
        pila.put(7)
        antes = pila_a_lista(pila)
        self.assertEqual(buscar_el_maximo(pila), 7)
        despues = pila_a_lista(pila)
        self.assertEqual(antes, despues)

    def test_varios_elementos(self) -> None:
        pila: Pila[int] = Pila()
        for elem in [1, 2, 3, 4, 5]:
            pila.put(elem)
        antes = pila_a_lista(pila)
        self.assertEqual(buscar_el_maximo(pila), 5)
        despues = pila_a_lista(pila)
        self.assertEqual(antes, despues)

    def test_números_negativos(self) -> None:
        pila: Pila[int] = Pila()
        for elem in [-1, -2, -3]:
            pila.put(elem)
        antes = pila_a_lista(pila)
        self.assertEqual(buscar_el_maximo(pila), -1)
        despues = pila_a_lista(pila)
        self.assertEqual(antes, despues)
