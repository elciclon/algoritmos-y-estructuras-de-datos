from queue import LifoQueue as Pila


def esta_bien_balanceada(s: str) -> bool:
    expresion: Pila[str] = Pila()
    esta_balanceada: bool = True
    for signo in s:
        if signo in ["(", ")"]:
            expresion.put(signo)

    parentesis_abiertos: int = 0
    parentesis_cerrados: int = 0
    while not expresion.empty():
        signo: str = expresion.get()
        if parentesis_abiertos == parentesis_cerrados and signo == "(":
            return False
        elif signo == ")":
            parentesis_cerrados += 1
        else:
            parentesis_abiertos += 1
    return parentesis_abiertos == parentesis_cerrados
