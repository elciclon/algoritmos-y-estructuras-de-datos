import unittest

from sala_de_escape import *


class sala_de_escapeTest(unittest.TestCase):
    def test_promedio_de_salidas(self):
        registro_test_amplio: dict[str, list[int]] = {
            # 5 éxitos: 45, 30, 55, 40, 35
            "Ana": [0, 45, 61, 30, 0, 55, 40, 0, 35],
            # 0 éxitos: todos fracasos (61)
            "Bruno": [61, 61, 61, 61, 61, 61, 61, 61, 61],
            # 8 éxitos: 10, 20, 15, 25, 30, 12, 18, 14
            "Carla": [10, 20, 0, 15, 25, 30, 12, 18, 14],
            # 0 éxitos: todas ausencias (0)
            "Diego": [0, 0, 0, 0, 0, 0, 0, 0, 0],
            # 5 éxitos: 35, 52, 47, 38, 33
            "Elena": [35, 52, 0, 61, 0, 0, 47, 38, 33],
            # 4 éxitos: 12, 28, 34, 29
            "Facundo": [12, 61, 28, 0, 34, 0, 0, 0, 29],
            # 0 éxitos: ausencias y fracasos
            "Gisela": [0, 0, 0, 0, 61, 61, 61, 61, 0],
            # 5 éxitos: 60, 59, 58, 55, 57
            "Hugo": [60, 59, 58, 61, 0, 0, 55, 0, 57],
            # 5 éxitos: 9, 14, 23, 46, 41
            "Irene": [9, 0, 14, 0, 61, 23, 0, 46, 41],
            # 0 éxitos: todas ausencias
            "Julio": [0, 0, 0, 0, 0, 0, 0, 0, 0],
        }
        promedios: dict[str, tuple[int, float]] = {
            "Ana": (5, 41.0),
            "Bruno": (0, 0.0),
            "Carla": (8, 18.0),
            "Diego": (0, 0.0),
            "Elena": (5, 41.0),
            "Facundo": (4, 25.75),
            "Gisela": (0, 0.0),
            "Hugo": (5, 57.8),
            "Irene": (5, 26.6),
            "Julio": (0, 0.0),
        }
        self.assertEqual(promedio_de_salidas(registro_test_amplio), promedios)

    def test_tiempo_mas_rapido(self):
        tiempos_salas: list[int] = [0, 61, 44, 0, 24, 12, 61, 12]
        self.assertEqual(tiempo_mas_rapido(tiempos_salas), 5)

    def test_racha_mas_larga(self):
        tiempos: list[int] = [0, 10, 15, 0, 18, 17, 19, 14, 11, 0, 61, 30, 31, 32, 0]
        tiempos_racha_final: list[int] = [
            0,
            12,
            11,
            0,
            61,
            20,
            0,
            61,
            15,
            23,
            27,
            30,
            45,
            40,
        ]
        self.assertEqual(racha_mas_larga(tiempos), (4, 8))
        self.assertEqual(racha_mas_larga(tiempos_racha_final), (8, 13))

    def test_escape_en_solitario(self):
        amigos_por_salas: list[list[int]] = [
            [0, 0, 15, 0],
            [0, 0, 0, 0],
            [0, 0, 61, 0],
            [0, 5, 10, 0],
            [1, 0, 20, 0],
            [0, 0, 30, 0],
        ]
        res: list[int] = [0, 2, 5]
        self.assertEqual(escape_en_solitario(amigos_por_salas), res)


if __name__ == "__main__":
    unittest.main(verbosity=2)
