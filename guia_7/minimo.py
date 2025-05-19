def minimo(s: list[int]) -> int:
    minimo: int = s[0]
    for elem in s:
        if elem < minimo:
            minimo = elem
    return minimo
