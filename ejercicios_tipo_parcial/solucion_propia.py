def maximas_cantidades_consecutivos(v: list[int]) -> dict[int, int]:

    res: dict[int, int] = {}
    subsecuencia: list[int] = []

    for indice in range(len(v)):
        if indice == len(v) - 1:
            if not (v[indice] in subsecuencia) and not (v[indice] in res.keys()):
                res[v[indice]] = 1
            elif (v[indice] in subsecuencia) and not (v[indice] in res.keys()):
                subsecuencia.append(v[indice])
                res[v[indice]] = len(subsecuencia)
            else:
                subsecuencia.append(v[indice])
                if len(subsecuencia) > res[v[indice]]:
                    res[v[indice]] = len(subsecuencia)

        if len(subsecuencia) == 0:
            subsecuencia.append(v[indice])
        elif not (v[indice] in subsecuencia):
            if not v[indice - 1] in res.keys():
                res[v[indice - 1]] = len(subsecuencia)
                subsecuencia = [v[indice]]
            else:
                if len(subsecuencia) > res[v[indice - 1]]:
                    res[v[indice - 1]] = len(subsecuencia)
                    subsecuencia = [v[indice]]
                else:
                    subsecuencia = [v[indice]]
        else:
            subsecuencia.append(v[indice])

    return res
