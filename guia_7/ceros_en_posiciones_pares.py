def ceros_en_posiciones_pares(s: list[int]):
    for indice in range(0, len(s)):
        if indice % 2 == 0:
            s[indice] = 0
