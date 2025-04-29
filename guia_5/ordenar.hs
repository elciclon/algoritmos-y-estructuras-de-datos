ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar xs = minimo xs : ordenar (quitar (minimo xs) xs)

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x : y : xs)
  | x < y = minimo (x : xs)
  | otherwise = minimo (y : xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x xs
  | xs == [x] = []
  | x == head xs = tail xs
  | otherwise = head xs : (quitar x (tail xs))
