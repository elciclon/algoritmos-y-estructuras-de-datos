from queue import LifoQueue as Pila


def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str) -> None:

    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    else:
        historial: Pila[str] = Pila()
        historial.put(sitio)
        historiales[usuario] = historial


def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    return historiales[usuario].get()


historiales: dict[str, Pila[str]] = {}

visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
