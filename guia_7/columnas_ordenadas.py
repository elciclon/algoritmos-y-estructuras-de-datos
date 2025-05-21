from ordenados import *

def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    columna: list[int] = []
    resultado: list[bool] = []
    for i in range(0,(len(m[0]))):
        columna = []
        for fila in m:
            columna.append(fila[i])
        resultado.append(ordenados(columna))
    return resultado
    