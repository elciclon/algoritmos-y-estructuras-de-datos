import unittest

from agrupar_por_longitud import *


class agrupar_por_longitudTest(unittest.TestCase):
    def test_agrupar_por_longitud(self):
        self.assertEqual(agrupar_por_longitud("archivo_2.txt"), {4: 2, 5: 3, 7: 1})


if __name__ == "__main__":
    unittest.main(verbosity=2)
