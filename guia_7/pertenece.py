def pertenece(s: list[int], e: int) -> bool:
    for elem in s:
        if e == elem:
            return True
    return False


def pertenece_2(s: list[int], e: int) -> bool:
    for i in range(0, len(s)):
        if e == s[i]:
            return True
    return False


def pertenece_3(s: list[int], e: int) -> bool:
    lista = s.copy()
    while len(lista) != 0:
        if e == lista.pop():
            return True
    return False
