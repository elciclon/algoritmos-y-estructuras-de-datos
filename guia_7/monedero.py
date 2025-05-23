def monedero():
    historial: list[str, int] = []
    movimiento: str = input("Operacion: ")
    while movimiento != "X":
        monto: int = input("Monto: ")
        historial.append((movimiento, monto))
        movimiento: str = input("Operacion: ")
    return historial


print(monedero())
