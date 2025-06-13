def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    puntajes: dict[str, int] = {}

    for jugador in estrategias.keys():
        puntaje: int = 0
        for rival in estrategias.keys():
            if jugador == rival:
                continue
            elif estrategias[jugador] == "me la banco y no me desvío":
                if estrategias[rival] == "me la banco y no me desvío":
                    puntaje -= 5
                else:
                    puntaje += 10
            else:
                if estrategias[rival] == "me la banco y no me desvío":
                    puntaje -= 15
                else:
                    puntaje -= 10

        puntajes[jugador] = puntaje

    return puntajes
