{-enMismoIntervalo: dados dos números reales, indica si están relacionados por la relación de equivalencia en R cuyas
clases de equivalencia son: (−∞, 3],(3, 7] y (7, ∞), o dicho de otra manera, si pertenecen al mismo intervalo-}
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y | (x <= 3) && (y <= 3) = True
enMismoIntervalo x y | (x > 3) && (x <= 7) && (y > 3) && (y <= 7) = True
enMismoIntervalo x y | (x > 7) && (y > 7) = True
enMismoIntervalo x y | otherwise = False
