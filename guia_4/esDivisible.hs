{-Ejercicio 3. Especificar e implementar la funcion esDivisible :: Integer ->Integer ->Bool que dados dos numeros
naturales determinar si el primero es divisible por el segundo. No está permitido utilizar las funciones mod ni div.
{problema esDivisible{a:N, b:N}:Bool
                        requiere:{True}
                        asegura: {a es divisible por b -> res = true}
                                 {a no es divisible por b -> res = false}
                        }
                        -}

esDivisible :: Integer -> Integer -> Bool
esDivisible a b
  | resto a b == 0 = True
  | otherwise = False

resto :: Integer -> Integer -> Integer
resto a b
  | a < b = a
  | otherwise = resto (a - b) b
