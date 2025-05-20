def long_mayor_a_siete(s: list[str]) -> bool:
    for elem in s:
        if len(elem) > 7:
            return True
    return False
