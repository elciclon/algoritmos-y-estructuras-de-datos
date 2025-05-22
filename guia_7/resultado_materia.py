def resultado_materia(notas: list[int]) -> int:
    acumulador: int = 0
    for indice in range(0, len(notas)):
        acumulador += notas[indice]
        if notas[indice] < 4:
            return 3
    if acumulador == 0:
        return 3
    promedio: float = float(acumulador) / (indice + 1)
    if promedio >= 7:
        return 1
    else:
        return 2
