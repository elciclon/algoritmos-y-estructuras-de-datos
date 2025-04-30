{-sumarElUltimo :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[|s| − 1], s) }
}
Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]-}

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo xs = sumarElUltimoAux (ultimo xs) xs

sumarElUltimoAux :: Integer -> [Integer] -> [Integer]
sumarElUltimoAux n [] = []
sumarElUltimoAux n (x : xs) = n + x : sumarElUltimoAux n xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs
