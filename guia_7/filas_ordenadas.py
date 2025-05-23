from ordenados import *


def filas_ordenadas(m: list[list[int]], res: list[bool]):
    for indice in range(0, len(m)):
        if ordenados(m[indice]):
            res.append(True)
        else:
            res.append(False)
