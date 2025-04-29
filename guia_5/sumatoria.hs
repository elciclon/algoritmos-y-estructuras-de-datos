{-sumatoria :: [Integer] -> Integer según la siguiente especificación:
problema sumatoria (s: seq⟨Z⟩) : Z {
requiere: { True }
asegura: { resultado =
P|s|−1
i=0 s[i] }
}-}
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x : xs) = sumatoria xs + x