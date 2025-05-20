def maximo(s: list[int]) -> int:
    maximo: int = s[0]
    for elem in s:
        if elem > maximo:
            maximo = elem
    return maximo
