def ordenados(s: list[int]) -> bool:
    for i in range(0, len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True
