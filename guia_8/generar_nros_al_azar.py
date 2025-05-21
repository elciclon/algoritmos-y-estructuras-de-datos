from queue import LifoQueue as Pila
import random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    for _ in range(cantidad):
        numero: int = random.randint(desde, hasta)
        res.put(numero)
    return res

print(generar_nros_al_azar(3, 2, 5).get())