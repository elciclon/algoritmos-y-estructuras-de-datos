import unittest

from existe_palabra import *


class existe_palabraTest(unittest.TestCase):
    def test_existe_palabra(self):
        self.assertTrue(existe_palabra("archivo.txt", "perro"))
        self.assertFalse(existe_palabra("archivo.txt", "bolsa"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
