-- digitoUnidades: dado un número entero, extrae su dígito de las unidades
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

digitoDecenas :: Int -> Int
digitoDecenas x = div (mod x 100) 10

digitoGeneral :: Int -> Int -> Int
digitoGeneral x i = div (mod x (10 ^ (i + 1))) (10 ^ i)