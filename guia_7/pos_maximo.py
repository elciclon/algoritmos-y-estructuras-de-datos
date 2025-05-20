from maximo import *


def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    return s.index(maximo(s))
