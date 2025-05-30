from queue import LifoQueue as Pila


def cantidad_elementos(p: Pila) -> int:
    copia_aux_pila: Pila = Pila()
    contador: int = 0
    while p.empty() == False:
        copia_aux_pila.put(p.get())
        contador += 1
    while not copia_aux_pila.empty():
        p.put(copia_aux_pila.get())
    return contador
