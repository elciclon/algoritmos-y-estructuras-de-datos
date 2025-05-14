from math import sqrt, floor

def es_primo(n: int) -> bool:
    if n == 0 or abs(n) == 1:
        return False
    for i in range(2, floor(sqrt(abs(n))) + 1) :
        if n % i == 0:
            return False
    return True

