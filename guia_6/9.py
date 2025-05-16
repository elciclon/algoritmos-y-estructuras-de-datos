"""
problema:rt(in x: Z,inout g:Z):Z{
    requiere: {True}
    modifica: {g}
    asegura: {res = x + g}
    }
"""


def rt(x: int, g: int) -> int:
    g = g + 1
    # Estado a
    # vale g == g@pre + 1
    return x + g


g: int = 0
"""
problema:ro(in x: Z):Z{
    requiere: {True}
    asegura : {res = x + g}
    }
"""


def ro(x: int) -> int:
    global g
    # Estado a
    # vale g == 0
    g = g + 1
    # Estado b
    # vale g == g@a + 1

    return x + g
