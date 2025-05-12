def es_nombre_largo(nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

print(es_nombre_largo("adrian"))
print(es_nombre_largo("Lu"))
