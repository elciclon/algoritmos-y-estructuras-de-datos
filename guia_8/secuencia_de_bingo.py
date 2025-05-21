from queue import Queue as Cola
from copiar_pila import *
import random

def secuencia_de_bingo() -> Cola[int]:
    lista: list[int] = list(range(100))
    random.shuffle(lista)
    res: Cola[int] = Cola()

    for numero in lista:
        res.put(numero)
    return res

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    # bolillero_copia: Cola[int] = copiar_pila(bolillero)
    jugadas: int = 0
    bingo_completo: int = 0

    while not bolillero.empty():
        elemento: int = bolillero.get()
        if elemento in carton:
            jugadas +=1
            bingo_completo += 1
        else:
            jugadas += 1
        if bingo_completo == 12:
            return jugadas
        