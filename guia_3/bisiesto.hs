type Anio = Integer

type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto a = not (mod a 4 == 0 || (mod a 400 /= 0 && mod a 100 == 0))