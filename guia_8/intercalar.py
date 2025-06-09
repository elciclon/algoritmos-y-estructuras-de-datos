from queue import LifoQueue as Pila
from copiar_pila import *


def intercalar(p1: Pila, p2: Pila) -> Pila:
    copia_p1: Pila = copiar_pila(p1)
    copia_p2: Pila = copiar_pila(p2)
    pila_aux: Pila = Pila()
    pila_res: Pila = Pila()

    while not copia_p2.empty():
        pila_aux.put(copia_p2.get())
        pila_aux.put(copia_p1.get())

    while not pila_aux.empty():
        pila_res.put(pila_aux.get())

    return pila_res


p1: Pila = Pila()
p2: Pila = Pila()
for i in range(1, 10, 2):
    p1.put(i)
    p2.put(i + 1)

pila_res: Pila = intercalar(p1, p2)

while not pila_res.empty():
    print(pila_res.get())
