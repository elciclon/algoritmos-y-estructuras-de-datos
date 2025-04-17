iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n digito = mod (div n (10 ^ (cantDigitos n - digito))) 10

cantDigitos :: Integer -> Integer
cantDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantDigitos (div n 10)
