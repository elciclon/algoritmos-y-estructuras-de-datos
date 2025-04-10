-- distancia: calcula la distancia euclídea entre dos puntos de R2--
type Dupla = (Float, Float)

distancia :: Dupla -> Dupla -> Float
distancia a b = sqrt ((fst a - fst b) ^ 2 + (snd a - snd b) ^ 2)