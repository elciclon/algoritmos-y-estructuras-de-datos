{-sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera
lista por un solo blanco en la lista resultado.-}
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x : []) = [x]
sacarBlancosRepetidos (x : y : xs)
  | x == ' ' && y == ' ' = sacarBlancosRepetidos (x : xs)
  | otherwise = x : sacarBlancosRepetidos (y : xs)
