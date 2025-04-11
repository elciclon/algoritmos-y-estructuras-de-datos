{-Ejercicio 3. Especificar e implementar la funcion esDivisible :: Integer ->Integer ->Bool que dados dos n´umeros
naturales determinar si el primero es divisible por el segundo. No está permitido utilizar las funciones mod ni div.-}
esDivisible :: Integer -> Integer -> Bool
esDivisible a b
  | a < b && a == 0 = True
  | a < b && a /= 0 = False