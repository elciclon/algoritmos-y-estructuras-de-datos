def alguno_es(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0


print(alguno_es(4.5, 0))
print(alguno_es(0, 0))
print(alguno_es(0, 4.5))
print(alguno_es(4.5, 5))
