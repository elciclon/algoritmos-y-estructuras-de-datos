-- productoInterno: calcula el producto interno entre dos tuplas de R × R.--
type Dupla = (Float, Float)

productoInterno :: Dupla -> Dupla -> Float
productoInterno a b = fst a * fst b + snd a * snd b