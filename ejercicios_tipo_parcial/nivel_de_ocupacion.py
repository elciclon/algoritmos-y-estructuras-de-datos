def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    promedio_por_piso: list[float] = []
    for piso in camas_por_piso:
        cantidad_de_camas: int = 0
        suma_de_ocupadas: int = 0
        for cama in piso:
            cantidad_de_camas += 1
            if cama:
                suma_de_ocupadas += 1
        promedio_por_piso.append(suma_de_ocupadas / cantidad_de_camas)

    return promedio_por_piso
