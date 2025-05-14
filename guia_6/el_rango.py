"""problema: el_rango(numero: R): None
requiere:{True}
asegura:{Imprime "Menor a 5" si numero < 5}
asegura:{Imprime "Entre 10 y 20" si 10 <= numero <= 20}
asegura:{Imprime "Mayor a 20" si numero > 20}"""


def el_rango(numero: int) -> None:
    if numero < 5:
        print("Menor a 5")
    elif 10 <= numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")


el_rango(4)
el_rango(11)
el_rango(23)
el_rango(7)
