from pertenece import pertenece


def pertenece_a_cada_uno_version_2(s: list[list[int]], e: int, res: list[bool]):
    for indice in range(0, len(s)):
        if e in s[indice]:
            res.append(True)
        else:
            res.append(False)
