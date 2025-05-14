"""problema: jubilacion(sexo: Char, edad: Z): None
requiere: {Sexo tiene que ser F o M}
requiere: {edad entre 0 y 118}
asegura: {Imprime "Andá de vacaciones si es femenino y tiene 60 o más, si es masculino y tiene 65 o más o si tiene menos
de 18}
asegura: {Imprime "Te toca trabajar" para cualquier otro caso}"""


def jubilacion(sexo: str, edad: int) -> None:
    if (edad < 18) or (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")


jubilacion("M", 5)
jubilacion("F", 17)
jubilacion("M", 18)
jubilacion("F", 23)
jubilacion("M", 63)
jubilacion("F", 60)
jubilacion("M", 65)
jubilacion("F", 65)
