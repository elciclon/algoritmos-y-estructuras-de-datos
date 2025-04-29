{-eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una ´unica aparici´on de cada elemento, eliminando
las repeticiones adicionales.-}
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos (x : []) = [x]
eliminarRepetidos (x : xs)
  | pertenece x xs == True = x : eliminarRepetidos (quitarTodos x xs)
  | otherwise = eliminarRepetidos xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e (x : [])
  | e == x = []
  | otherwise = [x]
quitarTodos e (x : xs)
  | e == x = quitarTodos e xs
  | otherwise = x : quitarTodos e xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x : xs) = e == x || pertenece e xs