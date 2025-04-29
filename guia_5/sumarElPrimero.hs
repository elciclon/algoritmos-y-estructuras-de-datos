{-sumarElPrimero :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[0], s) }
}
Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]-}

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x : xs) = primero [x] (x : xs)

primero :: [Integer] -> [Integer] -> [Integer]
primero [n] [] = []
primero [n] (x : xs) = n + x : primero [n] xs