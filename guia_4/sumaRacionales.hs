sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumatoriaInterna 1 m
sumaRacionales n m = sumatoriaInterna n m + sumaRacionales (n - 1) m

sumatoriaInterna :: Integer -> Integer -> Float
sumatoriaInterna n 1 = fromIntegral n
sumatoriaInterna n m = fromIntegral n / fromIntegral m + sumatoriaInterna n (m - 1)
