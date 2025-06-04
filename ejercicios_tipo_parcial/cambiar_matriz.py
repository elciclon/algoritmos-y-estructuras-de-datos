def cambiar_matriz(A: list[list[int]]):
    candidatos: list[int] = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            candidatos.append(A[i][j])

    for i in range(len(A)):
        for j in range(len(A[0])):
            encontre: bool = False
            elemento: int =A[i][j]
            indice: int = 0
            while not encontre:
                if candidatos[indice] != elemento:
                    A[i][j] = candidatos[indice]
                    encontre = True
                    candidatos.pop(indice)
                indice += 1