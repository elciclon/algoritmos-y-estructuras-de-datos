"""problema: devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: Z): Z {
    requiere:{True}
    asegura: { res = 3 * n si n = k * 9 o res = 2 * n si n = k * 3 o res = n si n no cumple las condiciones anteriores }
}
"""


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 9 == 0:
        return numero * 3
    elif numero % 3 == 0:
        return numero * 2
    else:
        return numero


print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(6))
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(2))
