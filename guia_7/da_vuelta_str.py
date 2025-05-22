def da_vuelta_str(s: str) -> str:
    palabra: str = ""
    for letra in s:
        palabra = letra + palabra
    return palabra
