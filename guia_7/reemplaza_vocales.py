def reemplaza_vocales(s: str) -> str:
    palabra_sin_vocales: str = ""
    for letra in s:
        if letra not in "aeiou":
            palabra_sin_vocales += letra
        else:
            palabra_sin_vocales += "_"
    return palabra_sin_vocales
