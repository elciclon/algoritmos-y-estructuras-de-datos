import unittest

from pertenece import pertenece, pertenece_2, pertenece_3
from divide_a_todos import *


class Test_pertenece(unittest.TestCase):
    def test_pertenece_lista_vacia(self):
        self.assertFalse(pertenece([], 1))

    def test_pertenece(self):
        self.assertTrue(pertenece([1, 2, 3, 4, 5], 3))

    def test_no_pertenece(self):
        self.assertFalse(pertenece([1, 2, 3, 4, 5], 7))


class Test_pertenece_2(unittest.TestCase):
    def test_pertenece_lista_vacia_2(self):
        self.assertFalse(pertenece_2([], 1))

    def test_pertenece_2(self):
        self.assertTrue(pertenece_2([1, 2, 3, 4, 5], 3))

    def test_no_pertenece_2(self):
        self.assertFalse(pertenece_2([1, 2, 3, 4, 5], 7))


class Test_pertenece_3(unittest.TestCase):
    def test_pertenece_lista_vacia_3(self):
        self.assertFalse(pertenece_3([], 1))

    def test_pertenece_3(self):
        self.assertTrue(pertenece_3([1, 2, 3, 4, 5], 3))

    def test_no_pertenece_3(self):
        self.assertFalse(pertenece_3([1, 2, 3, 4, 5], 7))


class Test_divide_a_todos(unittest.TestCase):
    def test_divide_a_todos_lista_vacia(self):
        self.assertTrue(divide_a_todos([], 1))

    def test_divide_a_todos_1(self):
        self.assertTrue(divide_a_todos([1, 2, 3, 4, 5], 1))
        self.assertTrue(divide_a_todos([1, 2, 3, 4, 5], -1))

    def test_divide_a_todos(self):
        self.assertTrue(divide_a_todos([2, 4, 6, 8, 10, 12], 2))
        self.assertFalse(divide_a_todos([2, 4, 6, 8, 10, 12], 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
