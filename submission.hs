cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes d h = longitud (popularListaDivisores d h) 

popularListaDivisores :: Integer -> Integer -> [Integer]
popularListaDivisores _ 0 = []
popularListaDivisores d h | d == h && sumarDivisores (listarDivisores h (div h 2)) > h = [h]
                          | d == h && not (sumarDivisores (listarDivisores h (div h 2)) > h) = []
popularListaDivisores d h | sumarDivisores (listarDivisores h (div h 2)) > h = h: popularListaDivisores d (h - 1)
                          | otherwise = popularListaDivisores d (h -1)

sumarDivisores :: [Integer] -> Integer
sumarDivisores [] = 0
sumarDivisores (x:[]) = x
sumarDivisores (x:xs) = x + sumarDivisores xs

listarDivisores :: Integer -> Integer -> [Integer]
listarDivisores x 0 = []
listarDivisores x 1 = [1] 
listarDivisores x d | esDivisor x d == True = d: listarDivisores x (d - 1) 
                    | otherwise = listarDivisores x (d - 1)

esDivisor :: Integer -> Integer -> Bool
esDivisor x d | mod x d == 0 = True
              | otherwise = False

longitud :: [Integer] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas [] = []
cursadasVencidas listado = eliminarRepetidas(cursadasVencidasAux listado)

cursadasVencidasAux :: [(String, Integer, Integer)] -> [String]
cursadasVencidasAux ((cursada, anio, cuatri):xs) | anio <= 2020 = cursada: cursadasVencidas xs 
                                              | anio == 2021 && cuatri <= 1 = cursada: cursadasVencidas xs 
                                              | otherwise = cursadasVencidas xs 

eliminarRepetidas :: [String] -> [String]
eliminarRepetidas [] = []
eliminarRepetidas (x:[]) = [x]
eliminarRepetidas (x:xs) | not (pertenece x xs) = x: eliminarRepetidas xs  
                         | otherwise = eliminarRepetidas xs

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece cursada (x:xs) | cursada == x = True
                         | otherwise = pertenece cursada xs

saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] u = []
saturarEnUmbralHastaNegativo numeros u = saturar (encontrarNegativo numeros) u
                                      
saturar :: [Integer] -> Integer -> [Integer]
saturar (x:[]) u | x > u = [u]
                 | otherwise = [x]
saturar (x:xs) u | x > u = u: saturar xs u
                 | otherwise = x: saturar xs u


encontrarNegativo :: [Integer] -> [Integer]
encontrarNegativo (x:[]) | x < 0 = []
                         | otherwise = [x]   
encontrarNegativo (x:xs) | x < 0 = []
                         | otherwise = x: encontrarNegativo xs   

cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] u = 1
cantidadParesColumna (x:xs) u | mod (devolverU x u) 2 == 0 = (cantidadParesColumna xs u) + 1
                              | otherwise = cantidadParesColumna xs u


devolverU :: [Integer] -> Integer -> Integer
devolverU fila u | u == 0 = head fila
                 | otherwise = devolverU (tail fila) (u - 1)


