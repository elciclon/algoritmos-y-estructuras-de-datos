{-
problema f2(i:N, q:R): Z {
    requiere : {True}
    asegura : {resultado = Sumatoria desde i=1 hasta n q^i}
    }
-}
f2 :: Float -> Int -> Float
f2 q 1 = q
f2 q i = q ^ i + f2 q (i - 1)