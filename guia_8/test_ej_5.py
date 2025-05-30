import unittest
from esta_bien_balanceada import *


class Test_esta_bien_balanceada(unittest.TestCase):
    def test_esta_bien_balanceada(self):
        self.assertTrue(esta_bien_balanceada("1 + (2 x 3 - (20 / 5))"))
        self.assertTrue(esta_bien_balanceada("10 * (1 + (2 * (-1)))"))
        self.assertFalse(esta_bien_balanceada("1 + ) 2 x 3 ( ()"))
