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

    def test_alarma_epidemiologica(self):
        registros: list[tuple[int, str]] = [
            (1, "gripe"),
            (2, "covid"),
            (3, "dengue"),
            (4, "covid"),
            (6, "covid"),
            (7, "gripe"),
            (8, "dengue"),
            (9, "covid"),
            (11, "dengue"),
        ]

        infecciosas: list[str] = ["covid", "dengue", "gripe", "sarampión"]

        umbral: float = 0.20

        resultado: dict[str, float] = {
            "covid": round(4 / 9, 2),
            "dengue": round(3 / 9, 2),
            "gripe": round(2 / 9, 2),
        }
        self.assertEqual(
            alarma_epidemiologica(registros, infecciosas, umbral), resultado
        )

    def test_empleado_del_mes(self):
        horas: dict[int, list[int]] = {
            101: [8, 9, 8, 10],  # total 35
            102: [9, 9, 9, 9],  # total 36
            103: [7, 8, 8, 10],  # total 33
            104: [9, 9, 9, 9],  # total 36
        }

        resultado_esperado: list[int] = [102, 104]

        self.assertEqual(empleado_del_mes(horas), resultado_esperado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
