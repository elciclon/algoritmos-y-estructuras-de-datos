posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z)
  | esPar x = 1
  | esPar y = 2
  | esPar z = 3
  | otherwise = 4

esPar :: Int -> Bool
esPar x = mod x 2 == 0
