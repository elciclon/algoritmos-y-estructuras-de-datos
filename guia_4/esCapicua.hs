{-Ejercicio 9. Especificar e implementar una función esCapicua :: Integer ->Bool que dado n ∈ N≥0 determina si n es
un número capicúa.-}
esCapicua :: Integer -> Bool
esCapicua n
  | n < 10 = True
  | mod n 10 == div n (10 ^ (cantDigitos n - 1)) = esCapicua (eliminaPrimeroUltimo n)
  | otherwise = False

cantDigitos :: Integer -> Integer
cantDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantDigitos (div n 10)

eliminaPrimeroUltimo :: Integer -> Integer
eliminaPrimeroUltimo n = div (mod n (10 ^ (cantDigitos n - 1))) 10