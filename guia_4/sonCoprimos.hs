sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b
  | a == b = False
  | a < b = divisoresDe a b a
  | otherwise = divisoresDe b a b

divisoresDe :: Integer -> Integer -> Integer -> Bool
divisoresDe _ _ 1 = True
divisoresDe x y z
  | mod x z == 0 && mod y z == 0 = False
  | otherwise = divisoresDe x y (z - 1)
