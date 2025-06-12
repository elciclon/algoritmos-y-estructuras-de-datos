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
        codigos_barra: list[int] = [
            101,
            100002,
            130,
            19011,
            99500,
            123007,
            41017,
            211,
            123004,
            456013,
        ]

        codigos_filtrados: list[int] = [101, 100002, 19011, 123007, 41017, 211, 456013]

        tipos_pacientes_atendidos: list[str] = [
            "pez",
            "perro",
            "gato",
            "perro",
            "loro",
            "gato",
            "perro",
            "perro",
            "gato",
            "hamster",
            "perro",
            "gato",
            "gato",
            "perro",
        ]

        grilla_horaria: list[list[str]] = [
            # 9 hs   10 hs  11 hs  12 hs  14 hs  15 hs  16 hs  17 hs
            ["Ana", "Ana", "Luis", "Ana", "Pablo", "Carlos", "Sofía"],  # 9
            ["Ana", "Luis", "Luis", "Luis", "Pablo", "Carlos", "Sofía"],  # 10
            ["Ana", "Ana", "Luis", "María", "Pablo", "Carlos", "Juan"],  # 11
            ["Ana", "Ana", "Luis", "Ana", "Pablo", "Carlos", "Sofía"],  # 12
            ["María", "Carlos", "Juan", "Ana", "Pablo", "Carlos", "Sofía"],  # 14
            ["María", "Carlos", "Luis", "Ana", "Pablo", "María", "Sofía"],  # 15
            ["María", "Carlos", "Juan", "Ana", "Pablo", "Carlos", "Sofía"],  # 16
            ["María", "Carlos", "Juan", "Ana", "Pablo", "Carlos", "Sofía"],  # 17
        ]

        turnos_cubiertos: list[tuple[bool, bool]] = [
            (True, True),  # Monday   – all “Ana”, all “María”
            (False, True),  # Tuesday  – morning mixed, afternoon all “Carlos”
            (True, False),  # Wednesday– morning all “Luis”, afternoon mixed
            (False, True),  # Thursday – morning mixed, afternoon all “Ana”
            (True, True),  # Friday   – all “Pablo” both halves
            (True, False),  # Saturday – morning all “Carlos”, afternoon mixed
            (False, True),  # Sunday   – morning mixed, afternoon all “Sofía”
        ]
        self.assertEqual(stock_productos(productos), min_max_productos)
        self.assertEqual(filtrar_codigos_primos(codigos_barra), codigos_filtrados)
        self.assertEqual(subsecuencia_mas_larga(tipos_pacientes_atendidos), 5)
        self.assertEqual(un_responsable_por_turno(grilla_horaria), turnos_cubiertos)


if __name__ == "__main__":
    unittest.main(verbosity=2)
