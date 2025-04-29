{-ultimo :: [t] -> t segun la siguiente especificacion:
problema ultimo (s: seq⟨T⟩) : T {
requiere: { |s| > 0 }
asegura: { resultado = s[|s| − 1] }
}
-}
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs

