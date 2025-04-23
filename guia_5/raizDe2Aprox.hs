{-
problema raizDe2Aprox(n:N):R{
    requiere:{True}
    asegura:{resultado=raíz cuadrada de 2 aproximada por 2 + 1/(an-1)}}
-}
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (calculaAn n) - 1


calculaAn :: Integer -> Float 
calculaAn 1 = 2
calculaAn n = 2 + 1/(calculaAn (n - 1))

