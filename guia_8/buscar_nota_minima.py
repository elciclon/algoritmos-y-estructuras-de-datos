from queue import Queue as Cola


def buscar_nota_minima(c: Cola[tuple[str, int]]) -> tuple[str, int]:
    res: tuple[str, int] = ("", 11)
    copia_aux_cola: Cola = Cola()
    while not c.empty():
        calificacion: tuple[str, int] = c.get()
        copia_aux_cola.put(calificacion)
        if calificacion[1] < res[1]:
            res = calificacion

    while not copia_aux_cola.empty():
        c.put(copia_aux_cola.get())

    return res
