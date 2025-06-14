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


def alarma_epidemiologica(
    registros: list[tuple[int, str]], infecciosas: list[str], umbral: float
) -> dict[str, float]:
    resultado_esperado: dict[str, float] = {}
    longitud_registros: int = len(registros)

    for infecciosa in registros:
        if infecciosa[1] not in resultado_esperado.keys():
            resultado_esperado[infecciosa[1]] = 1.0
        else:
            resultado_esperado[infecciosa[1]] += 1

    for infecciosa in resultado_esperado.keys():
        porcentaje: float = round(
            resultado_esperado[infecciosa] / longitud_registros, 2
        )
        if porcentaje >= umbral:
            resultado_esperado[infecciosa] = porcentaje

    return resultado_esperado
