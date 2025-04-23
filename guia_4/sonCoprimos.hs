-- sonCoprimos :: Integer -> Integer -> Bool
esMenor :: Integer -> Integer -> Bool
esMenor a b = a < b

esDivisor :: Integer -> Integer -> Bool
esDivisor n i
  | mod n i == 0 = True
  | otherwise = False