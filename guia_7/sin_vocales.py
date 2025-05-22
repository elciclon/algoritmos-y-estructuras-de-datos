def sin_vocales(s: str) -> str:
    palabra_sin_vocales: str = ""
    for letra in s:
        if letra not in "aeiou":
            palabra_sin_vocales += letra
    return palabra_sin_vocales
