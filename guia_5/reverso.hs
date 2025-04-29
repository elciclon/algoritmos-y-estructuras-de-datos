{-reverso :: [t] -> [t] seg´un la siguiente especificaci´on:
problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
}
-}
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x : xs) = ultimo xs : reverso (principio (x : xs))

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs

principio :: [t] -> [t]
principio [_] = []
principio (x : xs) = x : principio xs
