from typing import TextIO


def invertir_lineas(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    f: TextIO = open(nombre_archivo_entrada, "r", encoding="utf8")
    archivo_entrada: list[str] = f.readlines()
    f.close()

    f: TextIO = open(nombre_archivo_salida, "w", encoding="utf8")
    for i in range(len(archivo_entrada) - 1, -1, -1):
        f.write(archivo_entrada[i])
    f.close()

invertir_lineas("archivo_entrada.txt", "archivo_salida.txt")