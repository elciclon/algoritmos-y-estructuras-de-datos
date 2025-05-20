from minimo import *


def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    menor: int = minimo(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == menor:
            return i
