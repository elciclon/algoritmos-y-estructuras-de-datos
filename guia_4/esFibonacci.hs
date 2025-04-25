{-Ejercicio 17. Implementar la función esFibonacci :: Integer ->Bool según la siguiente especificación:
problema esFibonacci (n: Z) : B {
requiere: { n ≥ 0 }
asegura: { resultado = true ↔ n es algún valor de la secuencia de Fibonacci definida en el ejercicio 1}
}
-}

esFibonacci :: Integer -> Bool
esFibonacci n = fibonacciHastaN n 0

fibonacciHastaN :: Integer -> Integer -> Bool
fibonacciHastaN n i
  | i == n + 2 = False
  | fibonacciPatternMatching i == n = True
  | otherwise = fibonacciHastaN n (i + 1)

fibonacciPatternMatching :: Integer -> Integer
fibonacciPatternMatching 0 = 0
fibonacciPatternMatching 1 = 1
fibonacciPatternMatching n = fibonacciPatternMatching (n - 1) + fibonacciPatternMatching (n - 2)
