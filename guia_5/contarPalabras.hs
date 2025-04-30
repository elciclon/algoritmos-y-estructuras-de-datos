import Text.Read (Lexeme(Char))
{-contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que
tiene.-}
--contarPalabras :: [Char] -> Integer
--contarPalabras [] = 1
--contarPalabras(x:xs) = 1 + (x
limpiarTexto :: [Char] -> [Char]
limpiarTexto texto = 


{-sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera
lista por un solo blanco en la lista resultado.-}
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x : []) = [x]
sacarBlancosRepetidos (x : y : xs)
  | x == ' ' && y == ' ' = sacarBlancosRepetidos (x : xs)
  | otherwise = x : sacarBlancosRepetidos (y : xs)

borrarPrimerUltimoBlanco :: [Char] -> [Char]
borrarPrimerUltimoBlanco texto = borrarPrimerBlanco (borrarUltimoBlanco texto)

borrarPrimerBlanco :: [Char] -> [Char]
borrarPrimerBlanco (' ' : xs) = xs
borrarPrimerBlanco texto = texto

borrarUltimoBlanco :: [Char] -> [Char]
borrarUltimoBlanco [] = []
borrarUltimoBlanco [' '] = []
borrarUltimoBlanco (x : xs) = x : borrarUltimoBlanco xs

