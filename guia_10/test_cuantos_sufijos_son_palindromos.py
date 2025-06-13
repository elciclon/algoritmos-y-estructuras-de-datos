import unittest
from cuantos_sufijos_son_palindromos import *


class cuantos_sufijos_son_palindromosTest(unittest.TestCase):
    def test_cuantos_sufijos_son_palindromos(self):
        self.assertEqual(cuantos_sufijos_son_palindromos("neuquen"), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
