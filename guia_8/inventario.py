def agregar_producto(
    inventario: dict[str, dict[str, int | float]],
    nombre: str,
    precio: float,
    cantidad: int,
) -> None:
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}


def actualizar_stock(
    inventario: dict[str, dict[str, int | float]], nombre: str, cantidad: int
) -> None:
    inventario[nombre]["cantidad"] = cantidad


def actualizar_precio(
    inventario: dict[str, dict[str, int | float]], nombre: str, precio: float
) -> None:
    inventario[nombre]["precio"] = precio


def calcular_valor_inventario(inventario: dict[str, dict[str, int | float]]) -> float:
    valor_inventario: float = 0
    for item in inventario.values():
        valor_inventario += item["precio"] * item["cantidad"]
    return valor_inventario


inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
actualizar_precio(inventario, "Camisa", 30.0)
actualizar_precio(inventario, "Camisa", 20.0)
valor_total: float = calcular_valor_inventario(inventario)
print(valor_total)
