{-
problema sumatoriaDoble(n:N, m:N):N {
    requiere:{True}
    asegura:{Sumatoria desde i = 1 hasta n de sumatoria desde j = 1 hasta m de i^j}}
    -}

sumatoriaDoble :: Int -> Int -> Int
sumatoriaDoble 1 _ = 1
sumatoriaDoble n m = sumaInterna n m + sumaInterna (n - 1) m  

sumaInterna :: Int -> Int -> Int
sumaInterna n 1 = n
sumaInterna n m = n ^ m + sumaInterna n (m - 1)
