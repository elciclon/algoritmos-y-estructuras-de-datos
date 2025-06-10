from queue import Queue as Cola
from copiar_cola import *


def pacientes_urgentes(c: Cola[tuple[int, str, str]]) -> int:
    urgentes: int = 0
    copia_c = copiar_cola(c)

    while not copia_c.empty():
        if copia_c.get()[0] < 4:
            urgentes += 1

    return urgentes
