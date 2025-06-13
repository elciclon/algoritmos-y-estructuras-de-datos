import unittest

from torneo_de_gallinas import *


class torneo_de_gallinasTest(unittest.TestCase):
    def test_torneo_de_gallinas(self):
        estrategias: dict[str, str] = {
            "Alice": "me la banco y no me desvío",
            "Bob": "me la banco y no me desvío",
            "Charlie": "me desvío siempre",
            "Dana": "me desvío siempre",
            "Eve": "me la banco y no me desvío",
        }

        resultado_esperado: dict[str, int] = {
            "Alice": 10,
            "Bob": 10,
            "Charlie": -55,
            "Dana": -55,
            "Eve": 10,
        }
        self.assertEqual(torneo_de_gallinas(estrategias), resultado_esperado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
