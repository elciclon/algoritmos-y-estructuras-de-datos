{-Ejercicio 5. Implementar la función medioFact :: Integer ->Integer que dado n ∈ N calcula n!! = n(n−2)(n−4)· · · .
problema medioFact (n: Z) : Z {
    requiere: { n ≥ 0 }
    asegura: { resultado =
⌊
(n−1)/
2
⌋
i=0
(n − 2i) }
}
Por ejemplo:
medioFact 10 ❀ 10 ∗ 8 ∗ 6 ∗ 4 ∗ 2 ❀ 3840.
medioFact 9 ❀ 9 ∗ 7 ∗ 5 ∗ 3 ∗ 1 ❀ 945.
medioFact 0 ❀ 1.

-}
medioFact :: Integer -> Integer
medioFact n
  | n == 0 = 1
  | n == 1 = 1
  | otherwise = n * medioFact (n - 2)