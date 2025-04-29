{-quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado es igual a s pero sin el elemento e. }
}-}
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos e (x:[]) | e == x = []
                     | otherwise = [x]
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x:quitarTodos e xs

