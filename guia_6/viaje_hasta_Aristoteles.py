def viaje_hasta_Aristoteles(partida: int) -> None:
    partida -= 20
    while partida > -384:
        print(f"Viajó 20 años al pasado, estamos en el año: {partida}")
        partida -= 20


viaje_hasta_Aristoteles(2025)
