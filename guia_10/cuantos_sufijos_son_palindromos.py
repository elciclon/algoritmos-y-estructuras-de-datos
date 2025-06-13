from queue import Queue as Cola


def remover_primera_letra(texto: str) -> str:
    res: str = ""
    for i in range(1, len(texto)):
        res += texto[i]
    return res


def invertir_palabra(texto: str) -> str:
    res: str = ""
    for i in range(len(texto) - 1, -1, -1):
        res += texto[i]
    return res


def cuantos_sufijos_son_palindromos(texto: str) -> int:
    palabras: list[str] = [texto]
    contador: int = 0
    for i in range(len(texto) - 1):
        texto = remover_primera_letra(texto)
        palabras.append(texto)

    for palabra in palabras:
        if palabra == invertir_palabra(palabra):
            contador += 1

    return contador
