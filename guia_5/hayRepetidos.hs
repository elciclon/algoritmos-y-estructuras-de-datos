{-hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}-}
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (_:[]) = False
hayRepetidos (x:xs) | pertenece x xs == True = True
                    | otherwise = hayRepetidos xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x : xs) = e == x || pertenece e xs