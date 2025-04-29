{-principio :: [t] -> [t] según la siguiente especificación:
problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { |s| > 0 }
asegura: { resultado = subseq(s, 0, |s| − 1) }
}
-}
principio :: [t] -> [t]
principio [_] = []
principio (x : xs) = x : principio xs
