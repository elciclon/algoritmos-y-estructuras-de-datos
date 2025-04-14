{-Ejercicio 2. Implementar una función parteEntera :: Float ->Integer según la siguiente especificación:
problema parteEntera (x: R) : Z {
requiere: { x ≥ 0 }
asegura: { resultado ≤ x < resultado + 1 }
}
-}
parteEntera :: Float -> Int
parteEntera x
  | x < 1 = 0
  | otherwise = 1 + parteEntera (x - 1)


  