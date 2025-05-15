def despegar(n: int) -> None:
    while n >= 1:
        print(n)
        n -= 1
    print("Despegue")


def despegar_2(n: int) -> None:
    for i in range(n, 1, -1):
        print(i)

    print("Despegue")


despegar(10)

despegar_2(10)
