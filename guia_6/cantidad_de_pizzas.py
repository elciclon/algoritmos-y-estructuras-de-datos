from math import ceil


def cantidad_de_pizzas(comenzales: int, porciones: int) -> int:
    return ceil((comenzales * porciones) / 8)


print(cantidad_de_pizzas(2, 4))
print(cantidad_de_pizzas(3, 4))
print(cantidad_de_pizzas(4, 3))
print(cantidad_de_pizzas(4, 5))
