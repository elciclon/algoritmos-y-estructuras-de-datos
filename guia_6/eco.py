def eco() -> None:
    i = 1
    while i <= 10:
        print("eco")
        i += 1


def eco2() -> None:
    for i in range(0, 9):
        print("eco")


eco()

eco2()
