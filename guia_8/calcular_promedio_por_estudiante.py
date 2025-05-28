def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str,float]:
    for nota in notas:
        lista_de_estudiantes: list[str] = []
        if nota[0] not in lista_de_estudiantes:
            lista_de_estudiantes.append(nota[0])


    suma_de_notas: dict[str, tuple[float, int]] = {}
    for estudiante in lista_de_estudiantes:
        suma_de_notas[estudiante] = (0.0, 0)

    for nota in notas:
        if nota[0] in suma_de_notas:
            suma_de_notas[nota[0]][0] += nota[1]
            suma_de_notas[nota[0]][1] += 1
        
    promedios: dict[str, float] = {}
    for estudiante in lista_de_estudiantes:
        promedios[estudiante] = suma_de_notas[estudiante][0] / suma_de_notas[estudiante][1]

    return promedios

def calcular_promedio_por_estudiante_v2(notas: list[tuple[str, float]]) -> dict[str,float]:
    suma_notas: dict[str, float] = {}
    cantidad_notas: dict[str, int] = {}

    for estudiante, nota in notas:
        if estudiante not in suma_notas.keys():
            suma_notas[estudiante] = nota
            cantidad_notas[estudiante] = 1
        else:
            suma_notas[estudiante] += nota
            cantidad_notas[estudiante] += 1