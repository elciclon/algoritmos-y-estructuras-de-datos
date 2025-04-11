{-sumarSoloMultiplos: dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que
son múltiplos del número natural.
Por ejemplo:
sumarSoloMultiplos (10,-8,-5) 2 ⇝ 2
sumarSoloMultiplos (66,21,4) 5 ⇝ 0
sumarSoloMultiplos (-30,2,12) 3 ⇝ -18-}
type Terna = (Int, Int, Int)

sumarSoloMultiplos :: Terna -> Int -> Int
sumarSoloMultiplos (a, b, c) d = esMultiploDe a d + esMultiploDe b d + esMultiploDe c d

esMultiploDe :: Int -> Int -> Int
esMultiploDe x y
  | mod x y == 0 = x
  | otherwise = 0
