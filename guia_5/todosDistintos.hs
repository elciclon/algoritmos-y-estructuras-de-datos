{-todosDistintos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema todosDistintos (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = f alse ↔ existen dos posiciones distintas de s con igual valor }
}
-}
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (_:[]) = True
todosDistintos (x:xs) | pertenece x xs == True = False
                      | otherwise = todosDistintos xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x : xs) = e == x || pertenece e xs