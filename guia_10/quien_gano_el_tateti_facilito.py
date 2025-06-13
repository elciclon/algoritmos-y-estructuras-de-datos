def crear_columnas(tablero: list[list[str]]) -> list[list[str]]:
    columnas: list[list[str]] = []
    for col in range(len(tablero[0])):
        columna: list[str] = []
        for fila in range(len(tablero)):
            columna.append(tablero[fila][col])
        columnas.append(columna)
    return columnas


def tiene_3_consecutivas(columna: list[str], letra: str) -> bool:
    for i in range(len(columna) - 3):
        if columna[i] == columna[i + 1] == columna[i + 2] == letra:
            return True
    return False


def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> dict[str, int]:
    columnas: list[list[str]] = crear_columnas(tablero)
    ana: bool = False
    beto: bool = False
    for columna in columnas:
        if tiene_3_consecutivas(columna, "X"):
            ana = True
            break
    for columna in columnas:
        if tiene_3_consecutivas(columna, "O"):
            beto = True
            break

    if ana and (not beto):
        return 1
    elif (not ana) and beto:
        return 2
    elif ana and beto:
        return 3
    else:
        return 0
