def peso_pino(altura: float) -> int:
    if altura <= 3:
        return altura * 100 * 3
    return 9 * 100 + (altura - 3) * 200


def es_peso_util(peso: int) -> bool:
    return min(400, peso) == 400 and max(1000, peso) == 1000


def sirve_pino(altura: float) -> bool:
    return es_peso_util(peso_pino(altura))


print(peso_pino(5))
print(es_peso_util(800))
print(es_peso_util(1200))

print(sirve_pino(5))
print(sirve_pino(2))
