from queue import Queue as Cola


def copiar_cola(cola: Cola[int]) -> Cola[int]:
    cola_auxiliar: Cola[int] = Cola()
    cola_copiada: Cola[int] = Cola()

    # Invertir cola
    while not cola.empty():
        elemento: int = cola.get()
        cola_auxiliar.put(elemento)
        cola_copiada.put(elemento)

    while not cola_auxiliar.empty():
        elemento: int = cola_auxiliar.get()
        cola.put(elemento)

    return cola_copiada
