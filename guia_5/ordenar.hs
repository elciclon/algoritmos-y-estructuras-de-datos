ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar xs = minimo xs: ordenar (quitar (minimo xs) xs) 





