from queue import Queue as Cola
from armar_secuencia_de_bingo import *


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    numeros_a_descubrir: int = 12
    numero: int = 0

    while numeros_a_descubrir > 0:
        numero = bolillero.get()
        if numero in carton:
            numeros_a_descubrir -= 1
        jugadas += 1

    return jugadas


bolillero: Cola[int] = armar_secuencia_de_bingo()
carton: list[int] = [3, 6, 2, 87, 0, 99, 77, 33, 44, 22, 11, 12]

jugadas: int = jugar_carton_de_bingo(carton, bolillero)
