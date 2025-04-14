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
  | a < b = False
  | a == b = True
  | otherwise = esDivisible (a - b) b

