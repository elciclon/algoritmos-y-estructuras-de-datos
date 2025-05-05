{-problema hayQueCodificar (c: Char, mapeo: seq⟨Char x Char⟩ ) : Bool {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  asegura: {res = true <=> c es igual a la primera componente de alguna tupla de mapeo}
}
-}

hayQueCodificar :: Char -> [(Char,Char)] -> Bool
hayQueCodificar a (x:[]) | a == fst x = True
                         | otherwise = False
hayQueCodificar a (x:xs) | a == fst x = True
                         | otherwise = hayQueCodificar a xs

{-problema cuantasVecesHayQueCodificar (c: Char, frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Z {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  requiere: {c pertenece a frase}
  asegura: {(res = 0 y hayQueCodificar (c, mapeo) = false) o (res = cantidad de veces que c aparece en frase y hayQueCodificar (c, mapeo) = true)}
}
-}

cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char,Char)] -> Int
cuantasVecesHayQueCodificar c frase mapeo | hayQueCodificar c mapeo == False = 0
                                          | otherwise = contarApariciones c frase 

contarApariciones :: Char -> [Char] -> Int
contarApariciones c (x:[]) | c == x = 1
                           | otherwise = 0
contarApariciones c frase | c == head frase = 1 + contarApariciones c (tail frase)
                          | otherwise = contarApariciones c (tail frase)

{-problema laQueMasHayQueCodificar (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Char {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  requiere: {Existe al menos un c que pertenece a frase y hayQueCodificar(c, mapeo)=true}
  asegura: {res = c donde c es el caracter tal que cuantasVecesHayQueCodificar(c, frase, mapeo) es mayor a cualquier otro caracter perteneciente a frase}
  asegura: {Si existen más de un caracter c que cumple la condición anterior, devuelve el que aparece primero en frase }
-}

laQueMasHayQueCodificar :: [Char] -> [(Char,Char)] -> Char
laQueMasHayQueCodificar frase mapeo = maximoCodificables (agruparCodificables frase mapeo) frase

maximoCodificables :: [Char] -> [Char] -> Char
maximoCodificables (x:[]) frase = x
maximoCodificables (x:y:xs) frase | contarApariciones x frase > contarApariciones y frase = maximoCodificables (x:xs) frase
                                  | otherwise = maximoCodificables (y: xs) frase  

agruparCodificables :: [Char] -> [(Char,Char)] -> [Char]
agruparCodificables [] mapeo = []
agruparCodificables frase mapeo | hayQueCodificar (head frase) mapeo == True = head frase : agruparCodificables (tail frase) mapeo
                                | otherwise = agruparCodificables (tail frase) mapeo

{-problema codificarFrase (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : seq ⟨Char⟩ {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  asegura: {|res| = | frase|}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = true entonces res[i]= (mapeo[j])1, para un j tal que 0 <= j < |mapeo| y mapeo[j])0=frase[i]}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = false entonces res[i]= frase[i]}
} -}

codificarFrase :: [Char] -> [(Char,Char)] -> [Char]
codificarFrase [] mapeo = []
codificarFrase frase mapeo | hayQueCodificar (head frase) mapeo == True = codificarChar (head frase) mapeo: codificarFrase (tail frase) mapeo  
                           | otherwise = (head frase): codificarFrase (tail frase) mapeo 
codificarChar :: Char -> [(Char,Char)] -> Char
codificar c [] = ' '
codificarChar c mapeo | c == fst (head mapeo) = snd (head mapeo)  
                      | otherwise = codificarChar c (tail mapeo)

