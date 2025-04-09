f4 :: Float -> Float -> Float
f4 x y = (x+y)/2
{-Problema f4(x:R, y:R):R {
    Requiere:{True}
    Asegura:{Res=(x+y)/2}
    }
    -}

f5 :: (Float -> Float) -> Float
f5 (x, y) = (x+y)/2
{-Problema f5(t:R x R):R {
    Requiere:{True}
    Asegura:{Res=(t0+t1)/2}
    }
    -}    