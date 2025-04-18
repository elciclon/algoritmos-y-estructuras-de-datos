{-longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos.-}
longitud :: [t] -> Integer
longitud [] = 0
longitud (_ : xs) = 1 + longitud xs