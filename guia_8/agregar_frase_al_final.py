from typing import TextIO


def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    f: TextIO = open(nombre_archivo, "a", encoding="utf8")
    f.write(frase)
    f.close()


agregar_frase_al_final("archivo_entrada.txt", "Y esta la tercera\n")
