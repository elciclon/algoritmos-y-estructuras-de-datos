from queue import LifoQueue as Pila


def buscar_nota_maxima(p: Pila[tuple[str, int]]) -> tuple[str, int]:
    res: tuple[str, int] = ("", 0)
    copia_aux_pila: Pila = Pila()
    while not p.empty():
        calificacion: tuple[str, int] = p.get()
        copia_aux_pila.put(calificacion)
        if calificacion[1] > res[1]:
            res = calificacion

    while not copia_aux_pila.empty():
        p.put(copia_aux_pila.get())
    
    return res
