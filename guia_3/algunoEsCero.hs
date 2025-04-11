-- algunoEsCero: dados dos números racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching)
algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y
  | x == 0 || y == 0 = True
  | otherwise = False

algunoEsCero2 :: Float -> Float -> Bool
algunoEsCero2 0 _ = True
algunoEsCero2 _ 0 = True
algunoEsCero2 _ _ = False