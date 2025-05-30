from queue import LifoQueue as Pila
import random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    for _ in range(cantidad):
        numero: int = random.randint(desde, hasta)
        res.put(numero)
    return res

numeros: Pila[int] = generar_nros_al_azar(3, 2, 5)
print(numeros.get())
print(numeros.get())
print(numeros.get())