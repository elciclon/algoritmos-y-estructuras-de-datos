{-Especificar e implementar una función eAprox :: Integer ->Float que aproxime el valor del número e
a partir de la siguiente sumatoria:
eˆ(n) = sumatoria desde i=0 hasta n de 1/i!
i
problema eAprox(n:N): R {
    requiere:{True}
    asegura:{resultado=valor aproximado de n}
}
-}
e :: Float
e = eAprox 9

eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = (1 / (fromInteger (factorial n)) + eAprox (n - 1))

factorial :: Integer -> Integer
factorial n
  | n == 1 = 1
  | otherwise = n * factorial (n - 1)