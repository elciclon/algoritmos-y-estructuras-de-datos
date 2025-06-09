from queue import LifoQueue as Pila


def evaluar_expresion(s: str) -> float:
    expresion: list[str] = []
    numeros_y_operadores: str = ""
    numeros: Pila = Pila()
    resultado: float = 0.0
    for caracter in s:
        if caracter == " ":
            expresion.append(numeros_y_operadores)
            numeros_y_operadores = ""
        else:
            numeros_y_operadores += caracter
    expresion.append(s[len(s) - 1])
    for elem in expresion:
        if not (elem in "+-*/"):
            numeros.put(elem)
        else:
            if elem == "+":
                resultado = int(numeros.get()) + int(numeros.get())
                numeros.put(resultado)
            elif elem == "-":
                resultado = -1 * int(numeros.get()) + int(numeros.get())
                numeros.put(resultado)
            elif elem == "*":
                resultado = int(numeros.get()) * int(numeros.get())
                numeros.put(resultado)
            else:
                resultado = 1 / int(numeros.get()) * int(numeros.get())
                numeros.put(resultado)

    return resultado
