from columna import *


def chequea_verticales(m: list[list[str]], jugador: str) -> bool:
    for indice in range(0, 3):
        col: list[int] = columna(m, indice)
        if col[0] == col[1] == col[2] == jugador:
            return True
    return False


# def quien_gana_tateti(m: list[list[str]]) -> int:
