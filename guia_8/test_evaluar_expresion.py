import unittest
from evaluar_expresion import *


class evaluar_expressionTest(unittest.TestCase):

    def test_evaluar_expresion(self):
        self.assertEqual(evaluar_expresion("3 4 + 5 * 2 -"), 33.0)
        self.assertEqual(evaluar_expresion("33 4 + 5 * 2 -"), 183.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
