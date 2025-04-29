{-capicua :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema capicua (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { (resultado = true) ↔ (s = reverso(s)) }
}
Por ejemplo capicua [´a’,’c’, ’b’, ’b’, ’c’, ´a’] es true, capicua [´a’, ’c’, ’b’, ’d’, ´a’] es false.
-}
capicua :: (Eq t) => [t] -> Bool
capicua s = s == reverso s

reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x : xs) = ultimo xs : reverso (principio (x : xs))

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x : xs) = ultimo xs

principio :: [t] -> [t]
principio [_] = []
principio (x : xs) = x : principio xs
