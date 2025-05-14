from es_primo import es_primo

def cuantos_primos_en_rango(n: int, m: int) -> int:
    minimo = min(n,m)
    maximo = max(n,m)
    res = 0
    for i in range (minimo, maximo + 1):
        if es_primo(i):
            res += 1
    return res
    