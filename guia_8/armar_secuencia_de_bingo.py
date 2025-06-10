from queue import Queue as Cola
import random


def armar_secuencia_de_bingo() -> Cola[int]:
    lista_de_numeros: list[int] = []
    numeros: Cola[int] = Cola()
    contador: int = 0
    while contador < 100:
        numero: int = random.randint(0, 99)
        if not (numero in lista_de_numeros):
            lista_de_numeros.append(numero)
            contador += 1

    for elem in lista_de_numeros:
        numeros.put(elem)
    return numeros


armar_secuencia_de_bingo()
