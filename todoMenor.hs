todoMenor :: (Float, Float) -> (Float,Float) -> Bool
todoMenor(a,b) (c,d) = a < c && b < d

todoMenor :: (Float, Float) -> (Float,Float) -> Bool
todoMenor2 x y = fst(x)  < fst(y) && snd(x) < snd(y)