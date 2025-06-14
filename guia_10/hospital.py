from queue import Queue as Cola
from copiar_cola import *


def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    orden: Cola[int] = Cola()
    copy_urgentes: Cola[int] = copiar_cola(urgentes)
    copy_postergables: Cola[int] = copiar_cola(postergables)
    while not copy_urgentes.empty():
        orden.put(copy_urgentes.get())
        orden.put(copy_postergables.get())

    return orden
