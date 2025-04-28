quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x xs | xs == [x] = []
            | x == head xs = tail xs
            | otherwise = head xs:(quitar x (tail xs))