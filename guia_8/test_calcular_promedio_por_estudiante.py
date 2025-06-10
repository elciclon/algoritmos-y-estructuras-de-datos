import unittest

from calcular_promedio_por_estudiante import *


class calcular_promedio_por_estudianteTest(unittest.TestCase):
    def test_calcular_promedio_por_estudiante(self):

        notas: list[tuple[str, float]] = [
            ("Ana", 8.0),
            ("Juan", 7.5),
            ("Ana", 9.0),
            ("Pedro", 6.0),
            ("Juan", 8.5),
            ("Pedro", 7.0),
            ("Lucía", 10.0),
            ("Lucía", 9.5),
            ("Ana", 7.0),
            ("Pedro", 8.0),
        ]
        promedios: dict[str, float] = {
            "Ana": 8.0,  # (8.0 + 9.0 + 7.0) / 3
            "Juan": 8.0,  # (7.5 + 8.5) / 2
            "Pedro": 7.0,  # (6.0 + 7.0 + 8.0) / 3
            "Lucía": 9.75,  # (10.0 + 9.5) / 2
        }
        self.assertEqual(calcular_promedio_por_estudiante(notas), promedios)
        self.assertEqual(calcular_promedio_por_estudiante_v2(notas), promedios)


if __name__ == "__main__":
    unittest.main(verbosity=2)
