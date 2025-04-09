-- esMultiploDe: dados dos números naturales, decide si el primero es múltiplo del segundo--
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y
  | mod x y == 0 = True
  | otherwise = False