f1 :: Float -> Float
f1 n
  | n == 0 = 1
  | otherwise = 0

{-Problema f1(n:R):R {
    Requiere:{True}
    Asegura:{n = 0 -> res = 1 y n /= 0 -> res = 0}
                }-}

f2 :: Float -> Float
f2 n
  | n == 1 = 15
  | n == -1 = -15

{-
    {Problema f2(n:R):R {
        Requiere:{n = 1 o n = -1}
        Asegura:{n = 1 -> res = 15 y n = -1 -> res = -15}

    }}
    -}

f3 :: Float -> Float
f3 n
  | n <= 9 = 7
  | n >= 3 = 5

{-
    {Problema f3(n:R):R{
    Requiere:{True}
    Asegura:{n <= 9 -> res = 7 y n > 9 -> res = 5}}}
-}

f4 :: Float -> Float -> Float
f4 x y = (x + y) / 2

{-Problema f4(x:R, y:R):R {
    Requiere:{True}
    Asegura:{res=(x+y)/2}
    }
    -}

f5 :: (Float, Float) -> Float
f5 (x, y) = (x + y) / 2

{-Problema f5(t:R x R):R {
    Requiere:{True}
    Asegura:{res=(t0+t1)/2}
    }
    -}

f6 :: Float -> Int -> Bool
f6 a b = truncate a == b

{-
{Problema f6(a:R, b:Z):
    Requiere:{True}
    Asegura:{ si la parte entera de a = b -> res = true
    -}
