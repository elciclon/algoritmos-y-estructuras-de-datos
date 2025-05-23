from pertenece import pertenece


def pertenece_a_cada_uno_version_1(s: list[list[int]], e: int, res: list[bool]):
    for indice in range(0, len(s)):
        if pertenece(s[indice], e):
            res.append(True)
        else:
            res.append(False)
