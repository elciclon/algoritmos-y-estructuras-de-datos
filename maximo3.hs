maximo3 :: Int -> Int-> Int -> Int
maximo3 x y z = maximo2 (maximo2 x y) z

maximo2 :: Int -> Int-> Int
maximo2 x y | y > x = y
            | otherwise = x

