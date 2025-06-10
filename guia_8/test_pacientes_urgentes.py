import unittest
from pacientes_urgentes import *


class pacientes_urgentesTest(unittest.TestCase):
    def test_pacientes_urgentes(self):

        lista_de_pacientes = [
            (5, "Juan Pérez", "Fractura"),
            (2, "Ana Gómez", "Apendicitis"),
            (8, "Luis Torres", "Infarto"),
            (1, "María López", "Migraña"),
            (10, "Carlos Ruiz", "Quemaduras"),
            (4, "Sofía Díaz", "Asma"),
            (7, "Pedro Sánchez", "Accidente de tráfico"),
            (3, "Lucía Fernández", "Neumonía"),
            (9, "Miguel Castro", "Derrame cerebral"),
            (6, "Valeria Romero", "Hemorragia"),
        ]

        pacientes: Cola[tuple[int, str, str]] = Cola()
        for paciente in lista_de_pacientes:
            pacientes.put(paciente)

        self.assertEqual(pacientes_urgentes(pacientes), 3)
