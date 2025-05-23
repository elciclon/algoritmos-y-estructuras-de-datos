def estudiantes():
    estudiantes: list[str] = []
    estudiante: str = input("Ingrese los nombres de los estudiantes: ")
    while "" != estudiante != "listo":
        estudiantes.append(estudiante)
        estudiante: str = input("Ingrese los nombres de los estudiantes: ")
    return estudiantes


nombres: list[str] = estudiantes()
for nombre in nombres:
    print(nombre)
