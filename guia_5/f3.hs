{-
problema f3(q:R, n:Z): Z {
    requiere : {n>=0}
    asegura : {resultado = Sumatoria desde i=1 hasta 2n q^i}
    }
-}
f3 :: Float -> Int -> Float
f3 q 1 = q
f3 q n = q ^ (2 * n) + f3 q (2 * n) - 1