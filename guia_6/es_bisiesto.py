def es_bisiesto(anio: int) -> bool:
    return anio % 400 == 0 or (anio % 4 == 0 and not (anio % 100 == 0))


print(es_bisiesto(2025))
print(es_bisiesto(1600))
print(es_bisiesto(2026))
print(es_bisiesto(2024))
