type Punto2D = (Float, Float)

todoMenor :: Punto2D -> Punto2D -> Bool
todoMenor(a,b) (c,d) = a < c && b < d

todoMenor2 :: (Float, Float) -> (Float,Float) -> Bool
todoMenor2 x y = fst(x)  < fst(y) && snd(x) < snd(y)