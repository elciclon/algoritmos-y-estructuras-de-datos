-- sumaDistintos: que dados tres numeros enteros calcule la suma sin sumar repetidos (si los hubiera).--
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x == y) && (y == z) = x
sumaDistintos x y z | x == y = x + z
sumaDistintos x y z | x == z = x + y
sumaDistintos x y z | z == y = x + z
sumaDistintos x y z | otherwise = x + y + z