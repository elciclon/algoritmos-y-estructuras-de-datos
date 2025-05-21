import unittest

from columnas_ordenadas import *

class Test_columnas_ordenadas(unittest.TestCase):
    matriz_ordenada:list[list[int]] = [[1,2,3],[2,3,4],[3,4,5]]
    matriz_desordenada:list[list[int]] = [[2,3,4],[1,2,3],[3,4,5]]
    def test_columnas_ordenadas_longitud(self):
        longitud = len(columnas_ordenadas(self.matriz_ordenada))
        self.assertEqual(len(columnas_ordenadas(self.matriz_ordenada)), longitud)

    def test_columnas_ordenadas(self):
        self.assertEqual(columnas_ordenadas(self.matriz_ordenada), [True, True,True])
        self.assertNotEqual(columnas_ordenadas(self.matriz_desordenada), [True, True,True])
if __name__ == '__main__':
    unittest.main(verbosity=2)