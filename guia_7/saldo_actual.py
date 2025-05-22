def saldo_actual(movimientos: list[str, int]) -> int:
    saldo: int = 0
    for operacion, monto in movimientos:
        if operacion == "I":
            saldo += monto
        else:
            saldo -= monto
    return saldo
