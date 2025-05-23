import unittest

from pertenece_a_cada_uno_version_1 import *
from pertenece_a_cada_uno_version_2 import *
from pertenece_a_cada_uno_version_3 import *


class Test_pertenece_a_cada_uno_vesion_1(unittest.TestCase):
    lista_de_numeros: list[list[int]] = [
        [
            1,
            2,
            3,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]
    res: list = []

    def test_pertenece_a_cada_uno_vesion_1(self):
        pertenece_a_cada_uno_version_1(self.lista_de_numeros, 1, self.res)
        self.assertEqual(self.res, [True, False, False])
        self.res = []
        pertenece_a_cada_uno_version_1(self.lista_de_numeros, 2, self.res)
        self.assertEqual(self.res, [True, True, False])
        self.res = []
        pertenece_a_cada_uno_version_1(self.lista_de_numeros, 3, self.res)
        self.assertEqual(self.res, [True, True, True])
        self.res = []


class Test_pertenece_a_cada_uno_vesion_2(unittest.TestCase):
    lista_de_numeros: list[list[int]] = [
        [
            1,
            2,
            3,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]
    res: list = []

    def test_pertenece_a_cada_uno_vesion_2(self):
        pertenece_a_cada_uno_version_2(self.lista_de_numeros, 1, self.res)
        self.assertEqual(self.res, [True, False, False])
        self.res = []
        pertenece_a_cada_uno_version_2(self.lista_de_numeros, 2, self.res)
        self.assertEqual(self.res, [True, True, False])
        self.res = []
        pertenece_a_cada_uno_version_2(self.lista_de_numeros, 3, self.res)
        self.assertEqual(self.res, [True, True, True])
        self.res = []


class Test_pertenece_a_cada_uno_vesion_3(unittest.TestCase):
    lista_de_numeros: list[list[int]] = [
        [
            1,
            2,
            3,
        ],
        [2, 3, 4],
        [3, 4, 5],
    ]
    res: list = []

    def test_pertenece_a_cada_uno_vesion_3(self):
        self.assertEqual(
            pertenece_a_cada_uno_version_3(self.lista_de_numeros, 1),
            [True, False, False],
        )
        self.assertEqual(
            pertenece_a_cada_uno_version_3(self.lista_de_numeros, 2),
            [True, True, False],
        )
        self.assertEqual(
            pertenece_a_cada_uno_version_3(self.lista_de_numeros, 3),
            [True, True, True],
        )
