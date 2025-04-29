{-todosIguales :: (Eq t) => [t] -> Bool, 
que dada una lista devuelve verdadero s´ı y solamente s´ı todos sus elementos son iguales-}
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (_:[]) = True
todosIguales (x:xs) | x == head xs = todosIguales xs
                    | otherwise = False
