from math import sqrt


def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    min_max_productos: dict[str, tuple[int, int]] = {}

    for producto in stock_cambios:
        if not (producto[0] in min_max_productos.keys()):
            min_max_productos[producto[0]] = (producto[1], producto[1])
        else:
            if producto[1] < min_max_productos[producto[0]][0]:
                min_max_productos[producto[0]] = (
                    producto[1],
                    min_max_productos[producto[0]][1],
                )
            if producto[1] > min_max_productos[producto[0]][1]:
                min_max_productos[producto[0]] = (
                    min_max_productos[producto[0]][0],
                    producto[1],
                )

    return min_max_productos


def es_primo(numero: int) -> bool:
    for divisor in range(2, round(sqrt(numero) + 1)):
        if numero % divisor == 0:
            return False
    return True


def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    codigos_filtrados: list[int] = []
    for codigo in codigos_barra:
        if es_primo(codigo % 1000):
            codigos_filtrados.append(codigo)
    return codigos_filtrados


def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    subsecuencia: list[str] = []
    subsecuencia_mas_larga: list[str] = []
    indice: int = 0
    indice_subsecuencia: int = 0
    for paciente in tipos_pacientes_atendidos:
        if paciente in ["gato", "perro"]:
            subsecuencia.append(paciente)
        else:
            if len(subsecuencia) > len(subsecuencia_mas_larga):
                subsecuencia_mas_larga = subsecuencia
                subsecuencia = []
                indice_subsecuencia = indice - len(subsecuencia_mas_larga)
        indice += 1

    return indice_subsecuencia


def un_responsable_por_turno(
    grilla_horaria: list[list[str]],
) -> list[tuple[bool, bool]]:
    hay_un_responsable: list[tuple[bool, bool]] = []
    for columna in range(7):
        mañana: bool = False
        tarde: bool = False
        if (
            grilla_horaria[0][columna]
            == grilla_horaria[1][columna]
            == grilla_horaria[2][columna]
            == grilla_horaria[3][columna]
        ):
            mañana = True
        if (
            grilla_horaria[4][columna]
            == grilla_horaria[5][columna]
            == grilla_horaria[6][columna]
            == grilla_horaria[7][columna]
        ):
            tarde = True
        hay_un_responsable.append((mañana, tarde))

    return hay_un_responsable
