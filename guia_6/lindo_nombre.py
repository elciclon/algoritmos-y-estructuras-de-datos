"""problema: lindo_nombre(nombre: String): String {
requiere: {True}
asegura : {res: "Tu nombre tiene muchas letras!" si la longitud del nombre es mayor o igual a 5 caracteres}
asegura : {res = "Tu nombre tiene menos de 5 caracteres" si la longitud del nombre es menor que 5}}
"""


def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    return "Tu nombre tiene menos de 5 caracteres"


print(lindo_nombre("Adrián"))
print(lindo_nombre("Luna"))
