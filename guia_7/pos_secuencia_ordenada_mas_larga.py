def pos_secuencia_ordenada_mas_larga(s:list[int]) -> int:
    indice: int = 0
    secuencia_ordenada: list[int] = []
    secuencia_ordenada_mas_larg: list[int] = []
    for i in range(0, len(s)):
