import unittest

from quien_gano_el_tateti_facilito import *


class quien_gano_el_tateti_facilitoTest(unittest.TestCase):
    def test_quien_gano_el_tateti_facilito(self):
        tablero_res1: list[list[str]] = [
            ["X", " ", " ", " ", " "],
            ["X", "O", " ", " ", " "],
            ["X", " ", "O", " ", " "],
            [" ", "O", " ", " ", "X"],
            [" ", " ", " ", " ", " "],
        ]

        # Caso res = 2  → gana Beto (solo hay tres “O” consecutivas en una columna)
        tablero_res2: list[list[str]] = [
            ["X", "O", " ", " ", " "],
            [" ", "O", "X", " ", " "],
            [" ", "O", " ", "X", " "],
            ["X", " ", "O", " ", " "],
            [" ", " ", " ", " ", " "],
        ]

        # Caso res = 0  → nadie gana (no hay tres fichas consecutivas verticales)
        tablero_res0: list[list[str]] = [
            ["X", " ", " ", " ", " "],
            ["O", " ", " ", " ", " "],
            ["X", " ", " ", " ", " "],
            ["O", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
        ]

        # Caso res = 3  → trampa (hay tres “X” y tres “O” consecutivas verticales)
        tablero_res3: list[list[str]] = [
            ["X", " ", " ", " ", " "],
            ["X", " ", "O", " ", " "],
            ["X", " ", "O", " ", " "],
            [" ", " ", "O", " ", " "],
            [" ", " ", " ", " ", " "],
        ]

        resultados_esperados: dict[str, int] = {
            "tablero_res1": 1,
            "tablero_res2": 2,
            "tablero_res0": 0,
            "tablero_res3": 3,
        }
        self.assertEqual(quien_gano_el_tateti_facilito(tablero_res0), 0)
        self.assertEqual(quien_gano_el_tateti_facilito(tablero_res1), 1)
        self.assertEqual(quien_gano_el_tateti_facilito(tablero_res2), 2)
        self.assertEqual(quien_gano_el_tateti_facilito(tablero_res3), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
