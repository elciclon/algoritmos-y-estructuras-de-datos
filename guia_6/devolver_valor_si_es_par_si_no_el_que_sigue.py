"""problema: devolver_valor_si_es_par_si_no_el_que_sigue(n: Z): Z {
    requiere:{True}
    asegura: {res = n si n es par o n + 1 si n es impar }
}
"""


def devolver_valor_si_es_par_si_no_el_que_sigue(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    return numero + 1


print(devolver_valor_si_es_par_si_no_el_que_sigue(2))
print(devolver_valor_si_es_par_si_no_el_que_sigue(3))
