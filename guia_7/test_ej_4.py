import unittest

from saldo_actual import *


class Test_saldo_actual(unittest.TestCase):
    def test_saldo_actual(self):
        self.assertEqual(
            saldo_actual([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]), 1280
        )
        self.assertEqual(
            saldo_actual([("I", 200), ("R", 400), ("R", 1000), ("I", 300)]), -900
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
