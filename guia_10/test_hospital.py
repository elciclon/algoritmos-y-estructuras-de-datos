import unittest

from queue import Queue as Cola
from hospital import *


class hospitalTest(unittest.TestCase):
    def test_orden_de_atencion(self):
        urgentes: Cola[int] = Cola()
        urgentes.put(101)
        urgentes.put(102)
        urgentes.put(103)

        postergables: Cola[int] = Cola()
        postergables.put(201)
        postergables.put(202)
        postergables.put(203)

        orden_atencion: list[int] = [101, 201, 102, 202, 103, 203]

        orden: Cola[int] = orden_de_atencion(urgentes, postergables)

        indice: int = 0
        while not orden.empty():
            paciente: int = orden.get()
            self.assertEqual(paciente, orden_atencion[indice])
            indice += 1


if __name__ == "__main__":
    unittest.main(verbosity=2)
