from queue import Queue as Cola
from copiar_cola import *


def consolidar_prioridad(
    c: Cola[tuple[str, int, bool, bool]], res: Cola[tuple[str, int, bool, bool]]
):
    while not c.empty():
        res.put(c.get())


def atencion_a_clientes(
    c: Cola[tuple[str, int, bool, bool]],
) -> Cola[tuple[str, int, bool, bool]]:
    copia_de_c: Cola = copiar_cola(c)
    prioridad: Cola[tuple[str, int, bool, bool]] = Cola()
    preferencial: Cola[tuple[str, int, bool, bool]] = Cola()
    comun: Cola[tuple[str, int, bool, bool]] = Cola()
    res: Cola[tuple[str, int, bool, bool]] = Cola()

    while not copia_de_c.empty():
        cliente = copia_de_c.get()
        if cliente[3]:
            prioridad.put(cliente)
        elif cliente[2]:
            preferencial.put(cliente)
        else:
            comun.put(cliente)

    consolidar_prioridad(prioridad, res)
    consolidar_prioridad(preferencial, res)
    consolidar_prioridad(comun, res)

    return res
