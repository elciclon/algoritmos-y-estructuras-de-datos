def ceros_en_posiciones_pares_2(s: list[int]):
    copia_de_lista: list[int] = s.copy()
    for indice in range(0, len(copia_de_lista)):
        if indice % 2 == 0:
            copia_de_lista[indice] = 0
    return copia_de_lista
