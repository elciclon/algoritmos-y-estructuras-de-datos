from queue import Queue as Cola

from copiar_cola import *


def intercalar_cola(c1: Cola, c2: Cola) -> Cola:
    copia_c1: Cola = copiar_cola(c1)
    copia_c2: Cola = copiar_cola(c2)
    cola_res: Cola = Cola()

    numero: int = 0

    while not copia_c2.empty():
        numero = copia_c1.get()
        cola_res.put(numero)
        numero = copia_c2.get()
        cola_res.put(numero)

    return cola_res


c1: Cola = Cola()
c2: Cola = Cola()

for i in range(1, 10, 2):
    c1.put(i)
    c2.put(i + 1)

res: Cola = intercalar_cola(c1, c2)
while not res.empty():
    print(res.get())
