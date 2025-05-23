from columna import *


def transponer(m: list[list[int]]) -> list[list[int]]:
    matriz_transpuesta: list[list[int]] = []
    for col in range(0, len(m)):
        matriz_transpuesta.append(columna(m, col))
    return matriz_transpuesta
