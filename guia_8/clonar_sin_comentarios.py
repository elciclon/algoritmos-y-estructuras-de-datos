from typing import TextIO


def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str):
    archivo_entrada: TextIO = open(nombre_archivo_entrada, "r", encoding="utf-8")
    archivo_salida: TextIO = open(nombre_archivo_salida, "w", encoding="utf-8")
    for linea in archivo_entrada.readlines():

        for char in linea:
            if char != " " and char != "#":
                archivo_salida.write(linea)
                break
            elif char == "#":
                break

    archivo_entrada.close()
    archivo_salida.close()


clonar_sin_comentarios("archivo_con_comentarios.txt", "archivo_sin_comentarios.txt")
