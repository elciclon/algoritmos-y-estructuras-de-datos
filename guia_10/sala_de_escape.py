def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    rooms: dict[str, tuple[int, int]] = {}
    for amigo in registro.keys():
        rooms[amigo] = (0, 0)
        for tiempo in registro[amigo]:
            if tiempo > 0 and tiempo < 61:
                rooms[amigo] = (rooms[amigo][0] + tiempo, rooms[amigo][1] + 1)

    promedios: dict[str, tuple[int, float]] = {}
    for amigo in rooms.keys():
        if rooms[amigo][1] == 0:
            promedios[amigo] = (0, 0.0)
            continue
        else:
            promedios[amigo] = (rooms[amigo][1], rooms[amigo][0] / rooms[amigo][1])

    return promedios
