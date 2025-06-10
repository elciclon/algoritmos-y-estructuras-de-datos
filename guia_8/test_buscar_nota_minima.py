import unittest
from queue import Queue as Cola

from buscar_nota_minima import *


class buscar_nota_minimaTest(unittest.TestCase):
    def test_buscar_nota_minima(self):

        notas: Cola = Cola()
        notas.put(("SIlvina", 10))
        notas.put(("Luna", 9))
        notas.put(("Adrian", 3))
        notas.put(("Pepe", 4))
        notas.put(("Titi", 5))

        self.assertEqual(buscar_nota_minima(notas), ("Adrian", 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
