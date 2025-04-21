esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

menorDivisor :: Integer -> Integer
menorDivisor n = esMenor n 2

esMenor :: Integer -> Integer -> Integer
esMenor n i| esDivisor n 2 = 2
           | esDivisor n (i + 1) = i + 1
           | otherwise = esMenor n (i + 1)

esDivisor :: Integer -> Integer -> Bool 
esDivisor n i | mod n i == 0 = True
              | otherwise = False