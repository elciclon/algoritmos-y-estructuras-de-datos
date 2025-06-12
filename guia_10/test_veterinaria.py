import unittest
from veterinaria import *


class veterinariaTest(unittest.TestCase):
    def test_stock_de_productos(self):
        productos: list[tuple[str, int]] = [
            ("Croquetas", 50),
            ("Juguete", 10),
            ("Croquetas", 45),
            ("Alimento húmedo", 30),
            ("Juguete", 8),
            ("Medicamento", 20),
            ("Alimento húmedo", 35),
            ("Croquetas", 55),
            ("Medicamento", 18),
            ("Juguete", 12),
        ]
        min_max_productos: dict[str, tuple[int, int]] = {
            "Croquetas": (45, 55),
            "Juguete": (8, 12),
            "Alimento húmedo": (30, 35),
            "Medicamento": (18, 20),
        }
        self.assertEqual(stock_productos(productos), min_max_productos)


if __name__ == "__main__":
    unittest.main(verbosity=2)
