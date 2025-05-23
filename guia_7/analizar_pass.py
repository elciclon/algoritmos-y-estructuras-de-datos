def buscar_minusculas(password: str) -> int:
    for letra in password:
        if letra in "abcdefghijklmnopqrstuvwxyz":
            return 1
    return 0


def buscar_mayusculas(password: str) -> int:
    for letra in password:
        if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return 1
    return 0


def buscar_digitos(password: str) -> int:
    for letra in password:
        if letra in "0123456789":
            return 1
    return 0


def analizar_pass(password: str) -> str:
    if len(password) < 5:
        return "ROJA"
    puntaje: int = 0
    puntaje += buscar_minusculas(password)
    puntaje += buscar_mayusculas(password)
    puntaje += buscar_digitos(password)
    if puntaje == 3:
        return "VERDE"
    return "AMARILLA"


password: str = input("Ingrese su contraseña: ")
print(analizar_pass(password))
