import random

cartas: list[int] = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
jugadas: list[int] = []
suma_de_cartas: float = 0


def jugar_partida() -> bool:
    global suma_de_cartas
    jugada: int = random.choice(cartas)
    jugadas.append(jugada)
    print("Primera carta :" + str(jugada))
    opcion: str = input("Qué hacemos? ")
    while not opcion == "plantarse":
        jugada: int = random.choice(cartas)
        print("Tu carta: " + str(jugada))
        jugadas.append(jugada)
        for carta in jugadas:
            if carta <= 7:
                suma_de_cartas += carta
            else:
                suma_de_cartas += 0.5
        if suma_de_cartas > 7.5:
            return False
        opcion: str = input("Qué hacemos? ")
    return True


partida: bool = jugar_partida()
if partida == False:
    print("te pasaste")
    print(jugadas)
else:
    print("ganaste!!!!")
    print(jugadas)
