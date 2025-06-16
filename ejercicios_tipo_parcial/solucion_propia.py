from math import sqrt


def maximas_cantidades_consecutivos(v: list[int]) -> dict[int, int]:

    res: dict[int, int] = {}
    subsecuencia: list[int] = []

    for indice in range(len(v)):
        if indice == len(v) - 1:
            if not (v[indice] in subsecuencia) and not (v[indice] in res.keys()):
                res[v[indice]] = 1
            elif (v[indice] in subsecuencia) and not (v[indice] in res.keys()):
                subsecuencia.append(v[indice])
                res[v[indice]] = len(subsecuencia)
            else:
                subsecuencia.append(v[indice])
                if len(subsecuencia) > res[v[indice]]:
                    res[v[indice]] = len(subsecuencia)

        if len(subsecuencia) == 0:
            subsecuencia.append(v[indice])
        elif not (v[indice] in subsecuencia):
            if not v[indice - 1] in res.keys():
                res[v[indice - 1]] = len(subsecuencia)
                subsecuencia = [v[indice]]
            else:
                if len(subsecuencia) > res[v[indice - 1]]:
                    res[v[indice - 1]] = len(subsecuencia)
                    subsecuencia = [v[indice]]
                else:
                    subsecuencia = [v[indice]]
        else:
            subsecuencia.append(v[indice])

    return res


def absoluto(numero: int) -> int:
    if numero < 0:
        return numero * -1
    else:
        return numero


def es_primo(numero: int) -> bool:
    if numero <= 1:
        return False
    for i in range(2, round(sqrt(absoluto(numero)) + 1)):
        if numero % i == 0:
            return False
    return True


def contar_primos(columna: list[int]) -> int:
    contador: int = 0
    for numero in columna:
        if es_primo(numero):
            contador += 1
    return contador


def devolver_columnas(indice_columna: int, matriz: list[list[int]]) -> list[int]:
    columna: list[int] = []
    for fila in matriz:
        columna.append(fila[indice_columna])
    return columna


def maxima_cantidad_primos(matriz: list[list[int]]) -> int:
    maxima_cantidad: int = 0
    for indice in range(len(matriz[0])):
        primos_en_columna: int = contar_primos(devolver_columnas(indice, matriz))
        if primos_en_columna > maxima_cantidad:
            maxima_cantidad = primos_en_columna

    return maxima_cantidad
