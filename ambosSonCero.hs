-- algunoEsCero: dados dos números racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching)
ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y
  | x == 0 && y == 0 = True
  | otherwise = False

ambosSonCero2 :: Float -> Float -> Bool
ambosSonCero2 0 0 = True
ambosSonCero2 _ _ = False
