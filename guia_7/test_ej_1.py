import unittest

from pertenece import *
from divide_a_todos import *
from suma_total import *
from ceros_en_posiciones_pares import *
from maximo import *
from minimo import *
from ordenados import *
from pos_maximo import *
from pos_minimo import *
from long_mayor_a_siete import *
from es_palindromo import *
from iguales_consecutivos import *
from vocales_distintas import *
from cantidad_digitos_impares import *



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
        mi_lista: list[int] = [5, -3, -1, 7, 0, 4]
        elemento: int = 7
        pertenece(mi_lista, elemento)
        self.assertEqual(mi_lista, [5, -3, -1, 7, 0, 4])


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
        mi_lista: list[int] = [5, -3, -1, 7, 0, 4]
        elemento: int = 7
        pertenece_2(mi_lista, elemento)
        self.assertEqual(mi_lista, [5, -3, -1, 7, 0, 4])


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
        mi_lista: list[int] = [5, -3, -1, 7, 0, 4]
        elemento: int = 7
        pertenece_3(mi_lista, elemento)
        self.assertEqual(mi_lista, [5, -3, -1, 7, 0, 4])


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
        self.assertEqual(suma_total([1, -2, 3, -5, 10]), 7)

    def test_suma_total_positivos_y_negativos_incorrecta(self):
        self.assertNotEqual(suma_total([1, -2, 3, -5, 10]), 8)


class Test_ceros_posiciones_pares(unittest.TestCase):
    lista: list[int] = [2, 3, 4, 5, 6, 7, 8, 9]

    def test_ceros_en_posiciones_pares_modifica_len(self):
        ceros_en_posiciones_pares(self.lista)
        self.assertEqual(len(self.lista), 8)

    def test_ceros_en_posiciones_pares(self):
        ceros_en_posiciones_pares(self.lista)
        self.assertEqual(self.lista, [0, 3, 0, 5, 0, 7, 0, 9])


class Test_maximo(unittest.TestCase):
    lista: list[int] = [2, 3, 4, 5, 15, 6, 7, 8, 9]

    def test_maximo_modifica_lista(self):
        maximo(self.lista)
        self.assertEqual(self.lista, [2, 3, 4, 5, 15, 6, 7, 8, 9])

    def test_maximo_un_elemento(self):
        self.assertEqual(maximo([3]), 3)

    def test_maximo_positivo(self):
        self.assertEqual(maximo(self.lista), 15)

    def test_maximo_negativo(self):
        self.assertEqual(maximo([-3, -6, -2, 0, -15, -22]), 0)


class Test_minimo(unittest.TestCase):
    lista: list[int] = [2, 3, 4, 5, 15, 6, 7, 8, 9]

    def test_minimo_modifica_lista(self):
        minimo(self.lista)
        self.assertEqual(self.lista, [2, 3, 4, 5, 15, 6, 7, 8, 9])

    def test_minimo_un_elemento(self):
        self.assertEqual(minimo([3]), 3)

    def test_minimo_positivo(self):
        self.assertEqual(minimo(self.lista), 2)

    def test_maximo_negativo(self):
        self.assertEqual(minimo([-3, -6, -2, 0, -15, -22]), -22)


class Test_ordenados(unittest.TestCase):
    lista: list[int] = [2, 3, 4, 5, 15, 6, 7, 8, 9]

    def test_ordenados_modifica_lista(self):
        ordenados(self.lista)
        self.assertEqual(self.lista, [2, 3, 4, 5, 15, 6, 7, 8, 9])

    def test_ordenados_lista_vacia(self):
        self.assertTrue(ordenados([]))

    def test_ordenados(self):
        self.assertTrue(ordenados([-8, -3, 0, 2, 4, 7]))
        self.assertFalse(ordenados([2, 4, 7, 4, -3, -8, 0]))

    def test_ordenados_repetidos(self):
        self.assertTrue(ordenados([-8, -3, 0, 2, 4, 4, 7]))
        self.assertFalse(ordenados([2, 4, 7, 4, -3, -8, 0]))


class Test_pos_maximo(unittest.TestCase):
    def test_pos_maximo_lista_vacia(self):
        self.assertEqual(pos_maximo([]), -1)

    def test_pos_maximo_un_elemento(self):
        self.assertEqual(pos_maximo([-1]), 0)

    def test_pos_maximo(self):
        self.assertEqual(pos_maximo([2, 4, 7, 4, -3, -8, 0]), 2)

    def test_pos_maximo_repetidos(self):
        self.assertEqual(pos_maximo([2, 4, 7, 4, -3, -8, 0, 7]), 2)


class Test_pos_minimo(unittest.TestCase):
    def test_pos_minimo_lista_vacia(self):
        self.assertEqual(pos_minimo([]), -1)

    def test_pos_minimo_un_elemento(self):
        self.assertEqual(pos_minimo([-1]), 0)

    def test_pos_minimo(self):
        self.assertEqual(pos_minimo([2, 4, 7, 4, -3, -8, 0]), 5)

    def test_pos_maximo_repetidos(self):
        self.assertEqual(pos_minimo([2, 4, 7, 4, -3, -8, 0, -8]), 7)


class Test_long_mayor_a_siete(unittest.TestCase):
    def test_long_mayor_a_siete(self):
        self.assertFalse(long_mayor_a_siete(["termo", "gato", "tener", "jirafa"]))
        self.assertTrue(
            long_mayor_a_siete(["termo", "gato", "murcielago", "tener", "jirafa"])
        )

    def test_long_mayor_a_siete_unico_elemento(self):
        self.assertTrue(long_mayor_a_siete(["murcielago"]))

    def test_long_mayor_a_siete_ultimo(self):
        self.assertTrue(
            long_mayor_a_siete(
                ["termo", "gato", "murcielago", "tener", "jirafa", "murcielago"]
            )
        )


class Test_es_palindromo(unittest.TestCase):
    def test_es_palindromo_lista_vacia(self):
        self.assertTrue(es_palindromo())

    def test_es_palindromo_una_letra(self):
        self.assertTrue(es_palindromo("a"))

    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("anilina"))

    def test_es_palindromo_lista_vacia(self):
        self.assertFalse(es_palindromo("tempera"))

class Test_cantidad_digitos_impares(unittest.TestCase):
    def test_cantidad_digitos_impares(self):
        self.assertEqual(cantidad_digitos_impares([57, 2383, 812,246]), 5)
    def test_cantidad_digitos_impares_cero(self):
        self.assertEqual(cantidad_digitos_impares([0]), 0)
    def test_cantidad_digitos_impares_lista_vacia(self):
        self.assertEqual(cantidad_digitos_impares([]), 0)
    def test_cantidad_digitos_impares_pares(self):
        self.assertEqual(cantidad_digitos_impares([28, 2282, 842,246]), 0)
    

class Test_iguales_consecutivos(unittest.TestCase):
    def test_iguales_consecutivos_lista_vacia(self):
        self.assertFalse(iguales_consecutivos([]))

    def test_iguales_consecutivos_un_elemento(self):
        self.assertFalse(iguales_consecutivos([2]))

    def test_iguales_consecutivos(self):
        self.assertTrue(iguales_consecutivos([3, 6, 3, 2, 6, 8, 6, 3, 9, 9, 9]))
        self.assertFalse(iguales_consecutivos([3, 6, 3, 2, 6, 8, 6, 3, 9, 9]))


class Test_vocales_distintas(unittest.TestCase):
    def test_vocales_distintas(self):
        self.assertTrue(vocales_distintas("caleidoscopio"))
        self.assertTrue(vocales_distintas("murcielago"))
        self.assertFalse(vocales_distintas("anana"))
        self.assertFalse(vocales_distintas("abracadabra"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
