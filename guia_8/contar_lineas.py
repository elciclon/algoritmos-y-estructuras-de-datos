def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contador: int = 0
    for linea in archivo:
        contador += 1
    archivo.close()
    return contador


    