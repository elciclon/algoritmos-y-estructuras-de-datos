{-productoria :: [Integer] -> Integer seg´un la siguiente especificaci´on:
problema productoria (s: seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { resultado =
Q|s|−1
i=0 s[i] }
}-}
productoria :: [Integer] -> Integer
productoria (x : []) = x
productoria (x : xs) = x * productoria xs
