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


def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    mas_rapido: int = 61
    indice: int = 0

    for i in range(len(tiempos_salas)):
        if tiempos_salas[i] < mas_rapido and tiempos_salas[i] != 0:
            mas_rapido = tiempos_salas[i]
            indice = i
    return indice


def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    indice_inicio: int = 0
    indice_fin: int = 0
    mas_larga: list[int] = []
    secuencia: list[int] = []
    longitud_tiempos: int = len(tiempos)

    for i in range(longitud_tiempos):
        if tiempos[i] == 0 or tiempos[i] == 61:
            if len(secuencia) > len(mas_larga):
                mas_larga = secuencia
                secuencia = []
                indice_fin = i - 1
                indice_inicio = i - len(mas_larga)
        elif i == (longitud_tiempos - 1):
            if len(secuencia) > len(mas_larga):
                mas_larga = secuencia
                indice_fin = i
                indice_inicio = i - len(mas_larga) + 1
        else:
            secuencia.append(tiempos[i])

    return (indice_inicio, indice_fin)


def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res: list[int] = []
    for i in range(len(amigos_por_salas)):
        if (
            amigos_por_salas[i][0] == 0
            and amigos_por_salas[i][1] == 0
            and amigos_por_salas[i][3] == 0
            and amigos_por_salas[i][2] != 0
        ):
            res.append(i)
    return res
