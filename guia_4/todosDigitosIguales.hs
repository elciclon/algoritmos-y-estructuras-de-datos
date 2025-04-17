{-Ejercicio 6. Implementar la función todosDigitosIguales :: Integer ->Bool que determina si todos los dígitos de un
número natural son iguales, es decir:
problema todosDigitosIguales (n: Z) : B {
requiere: { n > 0 }
asegura: { resultado = true ↔ todos los dígitos de n son iguales }
}
-}
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
  | n < 100 = True
  | mod n 10 /= mod (div n 10) 10 = False
  | otherwise = todosDigitosIguales (div n 10)
