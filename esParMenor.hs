{- esParMenor: dadas dos tuplas de R × R, decide si cada coordenada de la primera tupla es menor a la coordenada
correspondiente de la segunda tupla -}
type Dupla = (Float, Float)

esParMenor :: Dupla -> Dupla -> Bool
esParMenor a b = fst a < fst b && snd a < snd b