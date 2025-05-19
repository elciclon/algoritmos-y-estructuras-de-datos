def maximo(s: list[int]) -> int:
    maximo: int = 0
    for elem in s:
        if elem > maximo:
            maximo = elem
    return maximo
