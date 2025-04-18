{-pertenece :: (Eq t) => t -> [t] -> Bool según la siguiente especificación:
problema pertenece (e: T, s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ e ∈ s }
}
-}
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x : xs) = e == x || pertenece e (xs)