{-invertir :: (a, b) -> (b, a): invierte los elementos del par pasado como parámetro. Debe funcionar para elementos
de cualquier tipo-}
invertir :: (t0, t1) -> (t1, t0)
invertir (a, b) = (b, a)
