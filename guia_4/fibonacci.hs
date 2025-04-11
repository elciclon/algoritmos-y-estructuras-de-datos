{-Ejercicio 1. Implementar la función fibonacci:: Integer ->Integer que devuelve el i-ésimo número de Fibonacci.
Recordar que la secuencia de Fibonacci se define como:
fib(n) =
    0 si n = 0
    1 si n = 1
    f ib(n − 1) + f ib(n − 2) en otro caso
problema fibonacci (n: Z) : Z {
requiere: { n ≥ 0 }
asegura: { resultado = fib(n) }
}
-}

fibonacci :: Integer -> Integer
fibonacci n
  | n == 0 = 0
  | n == 1 = 1
  | otherwise = fibonacci (n - 1) + fibonacci (n - 2)