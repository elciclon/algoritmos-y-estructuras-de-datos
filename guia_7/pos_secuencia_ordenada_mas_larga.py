def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    indice: int = 0
    longitud: int = 0
    longitud_maxima: int = 0
    for i in range(0, len(s) - 1):
        if s[i] < s[i + 1]:
            longitud += 1
            if longitud > longitud_maxima:
                longitud_maxima = longitud
                indice = i + 1 - longitud
        else:
            longitud = 0
    return indice
