-- maximoAbsoluto: devuelve el maximo entre el valor absoluto de dos numeros enteros
maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y
  | absoluto y > absoluto x = absoluto y
  | otherwise = absoluto x

absoluto :: Int -> Int
absoluto x
  | x < 0 = -x
