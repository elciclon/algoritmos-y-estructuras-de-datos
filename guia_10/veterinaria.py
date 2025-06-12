from math import sqrt


def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    min_max_productos: dict[str, tuple[int, int]] = {}

    for producto in stock_cambios:
        if not (producto[0] in min_max_productos.keys()):
            min_max_productos[producto[0]] = (producto[1], producto[1])
        else:
            if producto[1] < min_max_productos[producto[0]][0]:
                min_max_productos[producto[0]] = (
                    producto[1],
                    min_max_productos[producto[0]][1],
                )
            if producto[1] > min_max_productos[producto[0]][1]:
                min_max_productos[producto[0]] = (
                    min_max_productos[producto[0]][0],
                    producto[1],
                )

    return min_max_productos


def es_primo(numero: int) -> bool:
    for divisor in range(2, round(sqrt(numero) + 1)):
        if numero % divisor == 0:
            return False
    return True


def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    codigos_filtrados: list[int] = []
    for codigo in codigos_barra:
        if es_primo(codigo % 1000):
            codigos_filtrados.append(codigo)
    return codigos_filtrados
