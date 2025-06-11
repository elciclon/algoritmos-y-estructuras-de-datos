from typing import TextIO


def la_palabra_mas_frecuente(nombre_archivo: str) -> str:

    f: TextIO = open(nombre_archivo, "r", encoding="utf8")
    lineas: list[str] = f.readlines()
    f.close()

    palabras: dict[str, int] = {}

    for linea in lineas:
        if linea in palabras.keys():
            palabras[linea] += 1
        else:
            palabras[linea] = 1
    mas_frecuente: str = ""
    contador: int = 0
    for palabra in palabras.keys():
        if palabras[palabra] > contador:
            mas_frecuente = palabra
            contador = palabras[palabra]
    res: str = ""            
    for letra in mas_frecuente:
        if letra == "\n":
            break
        res += letra
        
    return res
