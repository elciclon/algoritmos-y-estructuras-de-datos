import unittest

from es_multiplo_de import es_multiplo_de
from devolver_el_doble_si_es_par import devolver_el_doble_si_es_par
from fahrenheit_a_celsius import fahrenheit_a_celsius
from es_primo import es_primo
from cuantos_primos_en_rango import cuantos_primos_en_rango


class Test_es_multiplo_de(unittest.TestCase):
    def test_es_multiplo_cero_y_uno(self):
        self.assertTrue(es_multiplo_de(0, 5))
        self.assertFalse(es_multiplo_de(1, 5))
        self.assertTrue(es_multiplo_de(15, 1))

    def test_es_multiplo_valores_iguales(self):
        self.assertTrue(es_multiplo_de(8, 8))
        self.assertEqual(es_multiplo_de(12, 12), True)

    def test_es_multiplo_valores_distintos(self):
        self.assertTrue(es_multiplo_de(8, 2))
        self.assertFalse(es_multiplo_de(3, 2))


class Test_devolver_el_doble(unittest.TestCase):
    def test_devolver_el_doble_numero_impar(self):
        self.assertEqual(devolver_el_doble_si_es_par(3), 3)
        self.assertEqual(devolver_el_doble_si_es_par(11), 11)


class Test_fahrenheit_a_celsius(unittest.TestCase):
    def test_fahrenheit_a_celsius(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(140.0), 60.0)
        self.assertNotAlmostEqual(fahrenheit_a_celsius(140.0), 60.5)


class Test_es_primo(unittest.TestCase):
    def test_es_primo_1_y_cero(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(-1))

    def test_es_primo_positivo(self):
        self.assertFalse(es_primo(6))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(11))

    def test_es_primo_negativo(self):
        self.assertFalse(es_primo(-6))
        self.assertTrue(es_primo(-2))
        self.assertTrue(es_primo(-11))


class Test_cuantos_primos_en_rango(unittest.TestCase):
    def test_n_menor_m(self):
        self.assertEqual(cuantos_primos_en_rango(2, 7), 4)

    def test_n_igual_m(self):
        self.assertEqual(cuantos_primos_en_rango(5, 5), 1)
        self.assertEqual(cuantos_primos_en_rango(4, 4), 0)

    def test_n_mayor_m(self):
        self.assertEqual(cuantos_primos_en_rango(7, 2), 4)

    def test_n_pos_m_neg(self):
        self.assertEqual(cuantos_primos_en_rango(-3, 3), 4)

    def test_m_pos_n_neg(self):
        self.assertEqual(cuantos_primos_en_rango(3, -3), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
