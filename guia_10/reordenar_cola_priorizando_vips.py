from queue import Queue as Cola
from copiar_cola import *


def reordenar_cola_priorizando_vips(fila_clientes: Cola[tuple[str, str]]) -> Cola[str]:
    copia_fila_clientes: Cola[tuple[str, str]] = copiar_cola(fila_clientes)
    cola_vip: Cola[str] = Cola()
    cola_comun: Cola[str] = Cola()
    clientes_ordenados: Cola[str] = Cola()
    while not copia_fila_clientes.empty():
        cliente: tuple[str, str] = copia_fila_clientes.get()
        if cliente[1] == "vip":
            cola_vip.put(cliente[0])
        else:
            cola_comun.put(cliente[0])

    while not cola_vip.empty():
        clientes_ordenados.put(cola_vip.get())

    while not cola_comun.empty():
        clientes_ordenados.put(cola_comun.get())

    return clientes_ordenados
