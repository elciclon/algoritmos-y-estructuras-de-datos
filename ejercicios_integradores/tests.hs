import Test.HUnit
import SolucionT1


main = runTestTT tests

tests = test [
-- "nombre" ~: (funcion parametros) ~?= resultado_esperado
    "hayQueCodificar True" ~: hayQueCodificar 'c' [('c','k'),('d','b')] ~?= True
    ]