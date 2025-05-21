def cantidad_digitos_impares(numeros: list[int]) -> int:
    impares: int = 0
    for numero in numeros:
        while numero > 0:
            resto: int = numero % 10
            if resto % 2 != 0:
                impares += 1
            numero = numero // 10
    return impares



