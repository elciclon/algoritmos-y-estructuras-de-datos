import unittest

from resultado_materia import *


class Test_resultado_materia(unittest.TestCase):
    def test_resultado_materia_vacio(self):
        self.assertEqual(resultado_materia([]), 3)

    def test_resultado_materia_tiene_3(self):
        self.assertEqual(resultado_materia([10, 10, 3, 10]), 3)

    def test_resultado_materia_aprobado(self):
        self.assertEqual(resultado_materia([4, 5, 8, 6]), 2)

    def test_resultado_materia_promocionado(self):
        self.assertEqual(resultado_materia([10, 10, 4, 10]), 1)

    def test_resultado_materia_desastre(self):
        self.assertEqual(resultado_materia([0, 0, 0, 0]), 3)
