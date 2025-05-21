def vocales_distintas(s: str) -> bool:
    vocales: str = ""
    for letra in s:
        if letra in "aeiou" and not letra in vocales:
            vocales += letra
    if len(vocales) >= 3:
        return True
    else:
        return False
