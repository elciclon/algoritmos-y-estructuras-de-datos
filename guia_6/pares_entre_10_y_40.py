def pares_entre_10_y_40() -> None:
    i = 10
    while i <= 40:
        print(i)
        i += 2


def pares_entre_10_y_40_2() -> None:
    for i in range(10, 41, 2):
        print(i)


pares_entre_10_y_40()
pares_entre_10_y_40_2()
