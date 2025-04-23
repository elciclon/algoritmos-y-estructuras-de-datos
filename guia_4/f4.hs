{-
problema f3(q:R, n:Z): R {
    requiere : {n>=0}
    asegura : {resultado = Sumatoria desde i=n hasta 2n q^i}
    }
-}
f4 :: Float -> Int -> Float
f4 q 0 = 1
f4 q n = prepararParametros q n

prepararParametros :: Float -> Int -> (Float)
prepararParametros q n = f2 (q, n, 2 * n)

f2 :: (Float, Int, Int) -> Float
f2 (q, n, i)
  | i == n = q ^ n
  | otherwise = q ^ i + f2 (q, n, (i - 1))
