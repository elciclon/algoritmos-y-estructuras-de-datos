from queue import LifoQueue as Pila

def buscar_el_maximo(pila: Pila[int]) -> int:
    pila_auxiliar: Pila[int] = Pila()
    maximo: int = pila.get()
    pila_auxiliar.put(maximo)

    while not pila.empty():
        actual: int = pila.get()
        if actual >= maximo:
            maximo = actual
        pila_auxiliar.put(actual)

    while not pila_auxiliar.empty():
        pila.put(pila_auxiliar.get())
    
    return maximo