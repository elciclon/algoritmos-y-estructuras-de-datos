def pertenece(s: list[int], e: int) -> bool:
    for elem in s:
        if e == elem:
            return True
    return False


def pertenece_2(s: list[int], e: int) -> bool:
    for i in range(0, len(s) - 1):
        if e == s[i]:
            return True
    return False


def pertenece_3(s: list[int], e: int) -> bool:
    while len(s) != 0:
        if e == s.pop():
            return True
    return False
