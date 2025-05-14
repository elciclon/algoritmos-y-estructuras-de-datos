def viaje_en_el_tiempo(partida: int, llegada: int) -> None:
    while partida != llegada:
        partida -= 1
        print(f"Viajó un año al pasado, estamos en el año: {partida}")


viaje_en_el_tiempo(2025, 1972)
