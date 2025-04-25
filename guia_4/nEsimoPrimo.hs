{- Implementar la función nEsimoPrimo :: Integer ->Integer que devuelve el n-ésimo primo (n ≥ 1). Recordar que el
primer primo es el 2, el segundo es el 3, el tercero es el 5, et-}
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = contador n 2

contador :: Integer -> Integer -> Integer
contador 1 p = iterador p
contador n p | iterador p == p = contador(n - 1) (p + 1)
             | otherwise = contador n (p + 1)

iterador :: Integer -> Integer
iterador p | esPrimo p == True = p
           | otherwise = iterador (p + 1)

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

