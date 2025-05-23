def es_matriz(s: list[list[int]]) -> bool:
    if len(s) == 0:
        return False
    longitud_fila: int = len(s[0])
    for indice in range(1, len(s)):
        if not len(s[indice]) == longitud_fila:
            return False
    else:
        return True
