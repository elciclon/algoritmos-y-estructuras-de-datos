import unittest

from queue import Queue as Cola
from atencion_a_clientes import *
from copiar_cola import *


def son_colas_iguales(
    c1: Cola[tuple[str, int, bool, bool]], c2: Cola[tuple[str, int, bool, bool]]
) -> bool:
    c1_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c1)
    c2_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c2)

    while not c1_copia.empty():
        elem_c1: tuple[str, int, bool, bool] = c1_copia.get()
        elem_c2: tuple[str, int, bool, bool] = c2_copia.get()
        if elem_c1 != elem_c2:
            return False
    return True


class Test_atencion_a_clientes(unittest.TestCase):
    def test_con_una_prioridad(self):
        cola: Cola[tuple[str, int, bool, bool]] = Cola()
        cola.put(("Pablo", 47347784, True, False))
        cola.put(("Brunilda", 98756891, True, False))
        cola.put(("Kiara", 10245697, False, True))
        cola.put(("Tamara", 46343766, False, False))

        cola_ordenada: Cola[tuple[str, int, bool, bool]] = Cola()
        cola_ordenada.put(("Kiara", 10245697, False, True))
        cola_ordenada.put(("Pablo", 47347784, True, False))
        cola_ordenada.put(("Brunilda", 98756891, True, False))
        cola_ordenada.put(("Tamara", 46343766, False, False))

        self.assertTrue(son_colas_iguales(atencion_a_clientes(cola), cola_ordenada))


if __name__ == "_main_":
    unittest.main(verbosity=2)
