{-contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que
tiene.-}
contarPalabras :: [Char] -> Integer
{-sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera
lista por un solo blanco en la lista resultado.-}
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x : []) = [x]
sacarBlancosRepetidos (x : y : xs)
  | x == ' ' && y == ' ' = sacarBlancosRepetidos (x : xs)
  | otherwise = x : sacarBlancosRepetidos (y : xs)

borrarPrimerUltimoBlanco :: [Char] -> [Char]

borrarPrimerUltimoBlanco (x : xs)

borrarPrimerUltimoBlanco [] = []

borrarPrimerBlanco

borrarUltimoBlanco

{-longitud :: [t] -> Integer, que dada una lista devuelve su cantidad de elementos.-}
longitud :: [t] -> Integer
longitud [] = 0
longitud (_ : xs) = 1 + longitud xs
