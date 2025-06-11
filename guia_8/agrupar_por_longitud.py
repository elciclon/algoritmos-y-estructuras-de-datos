from typing import TextIO


def agrupar_por_longitud(nombre_de_archivo: str) -> dict[int, int]:
    f: TextIO = open(nombre_de_archivo, "r", encoding="utf8")
    texto: list[str] = f.readline()
    longitud_texto: int = len(texto)
    res: dict[int, int] = {}
    palabra: str = ""

    for indice in range(longitud_texto):
        if indice == longitud_texto - 1:
            longitud_palabra: int = len(palabra)
            if longitud_palabra in res.keys():
                res[longitud_palabra] += 1
            else:
                res[longitud_palabra] = 1

        if texto[indice] == " ":
            longitud_palabra: int = len(palabra)
            if longitud_palabra in res.keys():
                res[longitud_palabra] += 1
            else:
                res[longitud_palabra] = 1
            palabra = ""
        else:
            palabra += texto[indice]

    return res
