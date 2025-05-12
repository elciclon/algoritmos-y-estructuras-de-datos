def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0


def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)


print(es_par(4))
print(es_par(5))
