lampara :: (Char, Integer) -> Char
lampara (a, x) | a == 'A' && x == 1 = 'P'
               | a == 'P' && x == 1 = 'A'
               | x > 1 = lampara (a, x-2)


lampara2 :: Bool -> Int -> Bool
lampara2 e p | p == 0 = e
             |p > 0 = lampara2 (not e) (p-1)
