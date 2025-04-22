{-
problema f1(n:Z):Z{
    requiere : {n>=0}
    asegura : {resultado = Sumatoria desde i=0 hasta n 2^i}
    }
-}
f1 :: Int -> Int
f1 0 = 1
f1 n = 2 ^ n + f1 (n - 1)