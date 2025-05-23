import unittest

from columnas_ordenadas import *
from es_matriz import *
from filas_ordenadas import *
from columna import *
from transponer import *
from quien_gana_tateti import *


class Test_columna(unittest.TestCase):
    matriz: list[list[int]] = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    matriz_2: list[list[int]] = [[2, 3, 4], [1, 2, 3], [3, 4, 5]]

    def test_columna(self):
        self.assertEqual(columna(self.matriz, 1), [2, 3, 4])
        self.assertEqual(columna(self.matriz_2, 2), [4, 3, 5])


class Test_columnas_ordenadas(unittest.TestCase):
    matriz_ordenada: list[list[int]] = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    matriz_desordenada: list[list[int]] = [[2, 3, 4], [1, 2, 3], [3, 4, 5]]

    def test_columnas_ordenadas_longitud(self):
        longitud = len(columnas_ordenadas(self.matriz_ordenada))
        self.assertEqual(len(columnas_ordenadas(self.matriz_ordenada)), longitud)

    def test_columnas_ordenadas(self):
        self.assertEqual(columnas_ordenadas(self.matriz_ordenada), [True, True, True])
        self.assertNotEqual(
            columnas_ordenadas(self.matriz_desordenada), [True, True, True]
        )


class Test_es_matriz(unittest.TestCase):
    matriz: list[list[int]] = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    no_matriz: list[list[int]] = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [7, 8, 0, 9]]
    matriz_desordenada: list[list[int]] = [[2, 3, 4], [1, 2, 3], [3, 4, 5]]

    def test_es_matriz_vacia(self):
        self.assertFalse(es_matriz([]))

    def test_es_matriz(self):
        self.assertFalse(es_matriz(self.no_matriz))
        self.assertTrue(es_matriz(self.matriz))


class Test_filas_ordenadas(unittest.TestCase):
    lista_de_numeros: list[list[int]] = [
        [
            1,
            2,
            3,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]
    lista_de_numeros_desordenados: list[list[int]] = [
        [
            1,
            3,
            2,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]
    res: list[bool] = []

    def test_filas_ordenadas(self):
        filas_ordenadas(self.lista_de_numeros, self.res)
        self.assertEqual(self.res, [True, True, True])
        self.res = []
        filas_ordenadas(self.lista_de_numeros_desordenados, self.res)
        self.assertEqual(self.res, [False, True, True])
        self.res = []


class Test_transponer(unittest.TestCase):
    matriz1: list[list[int]] = [
        [
            1,
            2,
            3,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]
    matriz2: list[list[int]] = [
        [
            1,
            3,
            2,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]

    def test_transponer(self):
        self.assertEqual(transponer(self.matriz1), self.matriz1)
        self.assertEqual(transponer(self.matriz2), [[1, 2, 3], [3, 3, 4], [2, 4, 5]])


class Test_quien_gana_el_tateti(unittest.TestCase):
    def test_chequea_verticales(self):
        self.assertTrue(
            chequea_verticales([["O", "X", "O"], ["X", " ", "O"], [" ", "X", "O"]], "O")
        )
        self.assertFalse(
            chequea_verticales([["O", "X", "O"], ["X", " ", "O"], [" ", "X", "O"]], "X")
        )
        self.assertTrue(
            chequea_verticales([["O", "X", " "], ["O", "X", " "], ["O", " ", " "]], "O")
        )
        self.assertFalse(
            chequea_verticales([["O", "X", " "], ["O", "X", " "], ["O", " ", " "]], "X")
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
