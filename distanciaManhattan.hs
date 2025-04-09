distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = absoluto(x1 - y1) + absoluto(x2 - y2) + absoluto(x3 - y3) 

absoluto :: Float -> Float
absoluto x | x < 0 = -x
           | otherwise = x 
