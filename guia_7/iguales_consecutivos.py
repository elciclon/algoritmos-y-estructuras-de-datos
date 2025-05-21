def iguales_consecutivos(s: list[int]) -> bool:
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return True
    return False
