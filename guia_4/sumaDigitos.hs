{-Ejercicio 8. Especificar e implementar la función sumaDigitos :: Integer ->Integer que calcula la suma de dígitos de
un número natural. Para esta función pueden utilizar div y mod.
problema sumaDigitos(n:N):N {
    requiere:{True}
    asegura: res = la suma de cada uno de los dígitos de n}
-}

sumaDigitos :: Integer -> Integer
sumaDigitos n
  | n < 10 = n
  | otherwise = mod n 10 + sumaDigitos (div n 10)
