from typing import TextIO


def cantidad_de_apariciones(nombre_de_archivo: str, palabra: str) -> int:
    f: TextIO = open(nombre_de_archivo, "r", encoding="utf8")
    lineas: list[str] = f.readlines()
    f.close()
    contador: int = 0
    for linea in lineas:
        if palabra in linea:
            contador += 1
    return contador
