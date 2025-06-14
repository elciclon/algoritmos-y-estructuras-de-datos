from queue import Queue as Cola


def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    orden: Cola[int] = Cola()
    while not urgentes.empty():
        orden.put(urgentes.get())
        orden.put(postergables.get())

    return orden
