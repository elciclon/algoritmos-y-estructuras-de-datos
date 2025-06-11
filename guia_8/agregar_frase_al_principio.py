from typing import TextIO


def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    f: TextIO = open(nombre_archivo, "r", encoding="utf8")
    lineas: list[str] = f.readlines()
    f.close()

    f: TextIO = open(nombre_archivo, "w", encoding="utf8")
    f.write(frase + "\n")
    f.writelines(lineas)
    f.close()


agregar_frase_al_principio("archivo_entrada.txt", "Buenas!!!!")
