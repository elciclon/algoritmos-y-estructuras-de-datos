def columna(m: list[list[int]], c: int) -> list[int]:
    columna: list[int] = []
    for fila in m:
        columna.append(fila[c])
    return columna
