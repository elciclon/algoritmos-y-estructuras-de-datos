comparar :: Int -> Int -> Int
comparar a b | (digitoGeneral a 0 + digitoGeneral a 1) < (digitoGeneral b 0 + digitoGeneral b 1) = 1 
             | (digitoGeneral a 0 + digitoGeneral a 1) > (digitoGeneral b 0 + digitoGeneral b 1) = (-1)
             | otherwise = 0

digitoGeneral :: Int -> Int -> Int
digitoGeneral x i = div (mod x (10 ^ (i + 1))) (10 ^ i)