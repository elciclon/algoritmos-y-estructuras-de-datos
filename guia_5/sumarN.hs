{-sumarN :: Integer -> [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { T rue }
asegura: {|resultado| = |s| ∧ cada posici´on de resultado contiene el valor que hay en esa posici´on en s sumado
n }
}-}
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n (x : []) = [n + x]
sumarN n (x : xs) = (n + x) : sumarN n xs
