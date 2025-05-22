import unittest

from ceros_en_posiciones_pares import *
from ceros_en_posiciones_pares_2 import *
from sin_vocales import *
from reemplaza_vocales import *
from da_vuelta_str import *
from eliminar_repetidos import *


class Test_ceros_posiciones_pares(unittest.TestCase):
    lista: list[int] = [2, 3, 4, 5, 6, 7, 8, 9]

    def test_ceros_en_posiciones_pares_modifica_len(self):
        ceros_en_posiciones_pares(self.lista)
        self.assertEqual(len(self.lista), 8)

    def test_ceros_en_posiciones_pares(self):
        ceros_en_posiciones_pares(self.lista)
        self.assertEqual(self.lista, [0, 3, 0, 5, 0, 7, 0, 9])


class Test_ceros_posiciones_pares(unittest.TestCase):
    lista: list[int] = [2, 3, 4, 5, 6, 7, 8, 9]

    def test_ceros_en_posiciones_pares_2_modifica_lista(self):
        ceros_en_posiciones_pares_2(self.lista)
        self.assertEqual(self.lista, [2, 3, 4, 5, 6, 7, 8, 9])

    def test_ceros_en_posiciones_pares_2(self):
        self.assertEqual(
            ceros_en_posiciones_pares_2(self.lista), [0, 3, 0, 5, 0, 7, 0, 9]
        )


class Test_sin_vocales(unittest.TestCase):
    def test_sin_vocales_vacia(self):
        self.assertEqual(sin_vocales(""), "")

    def test_sin_vocales(self):
        self.assertEqual(sin_vocales("murcielago"), "mrclg")


class Test_reemplaza_vocales(unittest.TestCase):
    palabra = "murcielago"

    def test_reemplaza_vocales_modifica_lenght(self):
        reemplaza_vocales(self.palabra)
        self.assertEqual(len(self.palabra), len("murcielago"))

    def test_reemplaza_vocales_vacia(self):
        self.assertEqual(reemplaza_vocales(""), "")

    def test_reemplaza_vocales(self):
        self.assertEqual(reemplaza_vocales(self.palabra), "m_rc__l_g_")


class Test_da_vuelta_str(unittest.TestCase):
    palabra = "murcielago"

    def test_da_vuelta_str_modifica_lenght(self):
        da_vuelta_str(self.palabra)
        self.assertEqual(len(self.palabra), len("murcielago"))

    def test_da_vuelta_str(self):
        self.assertEqual(da_vuelta_str(self.palabra), "ogaleicrum")

    def test_da_vuelta_str_vacia(self):
        self.assertEqual(da_vuelta_str(""), "")


class Test_eliminar_repetidos(unittest.TestCase):

    def test_eliminar_repetidos(self):
        self.assertEqual(eliminar_repetidos("anana"), "an")
        self.assertEqual(eliminar_repetidos("abracadabra"), "abrcd")
        self.assertEqual(eliminar_repetidos("rocía"), "rocía")


if __name__ == "__main__":
    unittest.main(verbosity=2)
