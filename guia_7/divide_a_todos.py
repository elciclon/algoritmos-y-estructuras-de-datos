def divide_a_todos(s: list, e: int) -> bool:
    for elem in s:
        if elem % e != 0:
            return False
    return True
