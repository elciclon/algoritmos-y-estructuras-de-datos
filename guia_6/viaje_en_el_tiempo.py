def viaje_en_el_tiempo(partida: int, llegada: int) -> None:
    while partida != llegada:
        partida -= 1
        print(f"Viajó un año al pasado, estamos en el año: {partida}")


viaje_en_el_tiempo(2025, 1972)


def viaje_en_el_tiempo_2(partida: int, llegada: int) -> None:
    for i in range(partida - 1, llegada - 1, -1):
        print(f"Viajó un año al pasado, estamos en el año: {i}")


viaje_en_el_tiempo_2(2025, 1972)
