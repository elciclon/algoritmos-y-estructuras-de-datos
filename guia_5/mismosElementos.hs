{-mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero s´ı y solamente s´ı
ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:
problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa}
}
-}
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r = mismosElementosAux s r && mismosElementosAux r s

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux (x : []) r | pertenece x r = True
mismosElementosAux (x : xs) r
  | pertenece x r = mismosElementosAux xs r
  | otherwise = False

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x : xs) = e == x || pertenece e xs