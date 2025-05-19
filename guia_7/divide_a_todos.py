def divide_a_todos(s: list[int], e: int) -> bool:
    for elem in s:
        if elem % e != 0:
            return False
    return True
