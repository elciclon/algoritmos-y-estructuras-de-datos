from typing import TextIO

def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str):
    archivo_entrada: TextIO = open(nombre_archivo_entrada, 'r', encoding="utf-8")     
    archivo_salida: TextIO = open(nombre_archivo_entrada, 'w', encoding="utf-8")     
    for linea in archivo_entrada.readlines():
        for char in linea:
            if char != ' ' and char != '#':
                archivo_salida.write(linea)

    archivo_entrada.close()
    archivo_salida.close()