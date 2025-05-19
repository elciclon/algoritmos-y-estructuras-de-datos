import unittest

from pertenece import pertenece, pertenece_2, pertenece_3
from divide_a_todos import *
from suma_total import *
from ceros_en_posiciones_pares import *



class Test_pertenece(unittest.TestCase):
    def test_pertenece_un_elemento(self):
        self.assertTrue(pertenece([1], 1)) 

    def test_pertenece_lista_vacia(self):
        self.assertFalse(pertenece([], 1))

    def test_pertenece(self):
        self.assertTrue(pertenece([1, 2, 3, 4, 5], 3))

    def test_no_pertenece(self):
        self.assertFalse(pertenece([1, 2, 3, 4, 5], 7))

    def test_pertenece_lista_no_cambia(self):
        mi_lista: list[int] = [5, -3, -1, 7, 0,4]
        elemento: int = 7
        pertenece(mi_lista, elemento)
        self.assertEqual(mi_lista, [5, -3, -1, 7, 0,4])
class Test_pertenece_2(unittest.TestCase):
    def test_pertenece_un_elemento_2(self):
        self.assertTrue(pertenece_2([1], 1)) 

    def test_pertenece_lista_vacia_2(self):
        self.assertFalse(pertenece_2([], 1))

    def test_pertenece_2(self):
        self.assertTrue(pertenece_2([1, 2, 3, 4, 5], 3))

    def test_no_pertenece_2(self):
        self.assertFalse(pertenece_2([1, 2, 3, 4, 5], 7))

    def test_pertenece_lista_no_cambia_2(self):
        mi_lista: list[int] = [5, -3, -1, 7, 0,4]
        elemento: int = 7
        pertenece_2(mi_lista, elemento)
        self.assertEqual(mi_lista, [5, -3, -1, 7, 0,4])
class Test_pertenece_3(unittest.TestCase):
    def test_pertenece_un_elemento_3(self):
        self.assertTrue(pertenece_3([1], 1)) 

    def test_pertenece_lista_vacia_3(self):
        self.assertFalse(pertenece_3([], 1))

    def test_pertenece_3(self):
        self.assertTrue(pertenece_3([1, 2, 3, 4, 5], 3))

    def test_no_pertenece_3(self):
        self.assertFalse(pertenece_3([1, 2, 3, 4, 5], 7))

    def test_pertenece_lista_no_cambia_3(self):
        mi_lista: list[int] = [5, -3, -1, 7, 0,4]
        elemento: int = 7
        pertenece_3(mi_lista, elemento)
        self.assertEqual(mi_lista, [5, -3, -1, 7, 0,4])

class Test_divide_a_todos(unittest.TestCase):
    def test_divide_a_todos_lista_vacia(self):
        self.assertTrue(divide_a_todos([], 1))

    def test_divide_a_todos_1(self):
        self.assertTrue(divide_a_todos([1, 2, 3, 4, 5], 1))
        self.assertTrue(divide_a_todos([1, 2, 3, 4, 5], -1))

    def test_divide_a_todos(self):
        self.assertTrue(divide_a_todos([2, 4, 6, 8, 10, 12], 2))
        self.assertFalse(divide_a_todos([2, 4, 6, 8, 10, 12], 3))

class Test_suma_total(unittest.TestCase):
    def test_suma_total_vacia(self):
        self.assertEqual(suma_total([]), 0)
    def test_suma_total_un_elemento(self):
        self.assertEqual(suma_total([1]), 1)
    def test_suma_total_positivos_y_negativos(self):
        self.assertEqual(suma_total([1, -2,3, -5,10]), 7)
    def test_suma_total_positivos_y_negativos_incorrecta(self):
        self.assertNotEqual(suma_total([1, -2,3, -5,10]), 8)
        
class Test_ceros_posiciones_pares(unittest.TestCase):
    def test_ceros_en_posiciones_pares_modifica_len(self):
        lista = [2,3,4,5,6,7,8,9]
        ceros_en_posiciones_pares(lista)
        self.assertEqual(len(lista), 8)
    def test_ceros_en_posiciones_pares(self):
        lista = [2,3,4,5,6,7,8,9]
        ceros_en_posiciones_pares(lista)
        self.assertEqual(lista, [0,3,0,5,0,7,0,9])

if __name__ == "__main__":
    unittest.main(verbosity=2)
