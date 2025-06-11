from typing import TextIO


def existe_palabra(nombre_de_archivo: str, palabra: str) -> bool:
    f: TextIO = open(nombre_de_archivo, "r", encoding="utf8")
    lineas: list[str] = f.readlines()
    f.close()
    for linea in lineas:
        if palabra in linea:
            return True
    return False
