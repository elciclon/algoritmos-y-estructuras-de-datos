def eliminar_repetidos(s: str) -> str:
    palabra: str = ""
    for letra in s:
        if not letra in palabra:
            palabra += letra
    return palabra
