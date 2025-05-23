from columna import *


def chequea_verticales(m: list[list[str]], jugador: str) -> bool:
    for indice in range(0, 3):
        col: list[int] = columna(m, indice)
        if col[0] == col[1] == col[2] == jugador:
            return True
    return False


def chequea_horizontales(m: list[list[str]], jugador: str) -> bool:
    for fila in m:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True
    return False


def chequea_diagonales(m: list[list[str]], jugador: str) -> bool:
    if (m[0][0] == m[1][1] == m[2][2] == jugador) or (
        m[0][2] == m[1][1] == m[2][0] == jugador
    ):
        return True
    return False


def quien_gana_tateti(m: list[list[str]]) -> int:
    if (
        chequea_horizontales(m, "O")
        or chequea_verticales(m, "O")
        or chequea_diagonales(m, "O")
    ):
        return 0
    elif (
        chequea_horizontales(m, "X")
        or chequea_verticales(m, "X")
        or chequea_diagonales(m, "X")
    ):
        return 1
    else:
        return 2
