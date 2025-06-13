import unittest
from queue import Queue as Cola
from reordenar_cola_priorizando_vips import *


class reordenar_cola_priorizando_vipsTest(unittest.TestCase):
    def test_reordenar_cola_priorizando_vips(self):
        clientes: list[tuple[str, str]] = [
            ("Laura", "común"),
            ("Bruno", "vip"),
            ("Sofía", "común"),
            ("Miguel", "vip"),
            ("Ana", "común"),
            ("Carlos", "vip"),
        ]

        cola_clientes: Cola[tuple[str]] = Cola()
        for cliente in clientes:
            cola_clientes.put(cliente)

        clientes_ordenados: Cola[str] = reordenar_cola_priorizando_vips(cola_clientes)
        self.assertEqual(clientes_ordenados.get(), "Bruno")
        self.assertEqual(clientes_ordenados.get(), "Miguel")
        self.assertEqual(clientes_ordenados.get(), "Carlos")
        self.assertEqual(clientes_ordenados.get(), "Laura")
        self.assertEqual(clientes_ordenados.get(), "Sofía")
        self.assertEqual(clientes_ordenados.get(), "Ana")

        indice = 0
        while not cola_clientes.empty():
            self.assertEqual(cola_clientes.get(), clientes[indice])
            indice += 1


if __name__ == "__main__":
    unittest.main(verbosity=2)
