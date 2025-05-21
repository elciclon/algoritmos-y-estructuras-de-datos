from queue import LifoQueue as Pila

def copiar_pila(pila: Pila[int]) -> Pila[int]:
    pila_auxiliar: Pila[int] = Pila()
    pila_copiada: Pila[int] = Pila()

    # Invertir pila
    while not pila.empty():
        elemento: int = pila.get()
        pila_auxiliar.put(elemento)

    while not pila_auxiliar.empty():
        elemento: int = pila_auxiliar.get()
        pila_copiada.put(elemento)
        pila.put(elemento)

    return pila_copiada