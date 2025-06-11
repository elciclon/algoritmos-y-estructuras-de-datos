from typing import TextIO


def listar_textos_de_archivo(nombre_de_archivo: str) -> list[str]:
    f: TextIO = open(nombre_de_archivo, "rb")
    texto: str = f.read()
    f.close()
    cadena: str = ""
    lista_de_cadenas: list[str] = []
    for byte in texto:
        if (
            not chr(byte)
            in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _"
        ):
            if len(cadena) >= 5:
                lista_de_cadenas.append(cadena)
                cadena = ""
            else:
                cadena = ""
        else:
            cadena += chr(byte)

    return lista_de_cadenas


print(listar_textos_de_archivo("session.wav"))
