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


inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
