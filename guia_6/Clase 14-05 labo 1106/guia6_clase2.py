import math

def volumen_esfera(radio:float) -> float:
    #aproximamos pi a 3,14
    res: float = 4/3 * 3.14 * radio**3
    return res


def triada_pitagorica(a: int, b: int, c:int) -> bool:
    suma: int = a**2 + b**2
    res: bool = suma == c**2
    return res


def es_multiplo_de(n:int, m:int) -> bool:
    return n % m == 0

def devolver_el_doble_si_es_par(n:int) -> int:
    return n if n % 2 == 1 else n*2

def farenheit_a_celcius(n:float) -> float:
    return (n-32)*5/9 

# Aclaración: Extendimos el ejercicio en el laboratorio para que también se consideren los números negativos.
# Para nosotros, un número negativo es primo si su valor absoluto es un número primo.
def es_primo(n:int) -> bool:
    n = abs(n)
    if n == 0 or n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# Solucion sin el primer if y yendo de n a 2
def es_primo_2(n:int) -> bool:
    n = abs(n)
    # Si n = 0 o n = 1 no va a entrar en el for.
    for i in range(n-1,1, -1):
        if n % i == 0:
            return False
    # Si no encontramos ningun divisor entonces si el numero es mas grande que 1 es porque es un primo. Si es menor o igual son los casos del 1 y el 0 que no son primos.
    return n > 1 

def min(a,b):
    if a < b:
        return a
    else:
        return b

def cuantos_primos_en_rango(n:int,m:int) -> int:
    minimo = min(n,m)
    maximo = max(n,m)
    res = 0
    for i in range(minimo,maximo+1):
        if es_primo_2(i):
            res = res + 1
    return res