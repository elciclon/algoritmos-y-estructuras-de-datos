import numpy as np
from transponer import *


def exponenciacion_matriz(d: int, p: int) -> list[list]:
    matriz = np.random.randint(0, 9, (d, d))
    matriz_resultante = matriz.copy()
    celda: int = 0
    for indice in range(0, p - 1):
        matriz = matriz_resultante.copy()
        for fila_factor_1 in range(0, d):
            for fila_factor_2 in range(0, d):
                for columna in range(0, d):
                    celda += (
                        matriz[fila_factor_1][columna]
                        * transponer(matriz)[fila_factor_2][columna]
                    )
                matriz_resultante[fila_factor_1, fila_factor_2] = celda
                celda = 0
    return matriz_resultante


print(exponenciacion_matriz(100, 100))
