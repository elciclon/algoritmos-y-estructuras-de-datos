{-
problema f3(q:R, n:Z): R {
    requiere : {n>=0}
    asegura : {resultado = Sumatoria desde i=1 hasta 2n q^i}
    }
-}
f3 :: Float -> Int -> Float
f3 q n = f2 q (2 * n)

f2 :: Float -> Int -> Float
f2 q 1 = q ^ 1
f2 q i = q ^ i + f2 q (i - 1)
