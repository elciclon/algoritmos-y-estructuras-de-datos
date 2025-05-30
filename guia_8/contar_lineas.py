from typing import TextIO

def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo, "r", eoncoding="utf-8")
    res: int = len(archivo.readlines())
    archivo.close()
    return res


    