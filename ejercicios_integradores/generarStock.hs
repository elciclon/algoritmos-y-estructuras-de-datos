--["madera", "clavo", "pala", "clavo"]
--[("madera", 1),("clavo",2),("pala",1)]

--generarStock :: [String] -> [(String, Int)]

filtrarRepetidos :: [String] -> [String]
filtrarRepetidos (x:[]) = [x] 
filtrarRepetidos (pal:xs) | pertenece pal xs == True = pal: quitar pal xs
                          | otherwise = pal: filtrarRepetidos xs

quitar :: String -> [String] -> [String]
quitar palabra (_:[]) = []
quitar palabra (pal:xs) | palabra == pal = quitar palabra xs
                        | otherwise = pal: quitar palabra xs

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece palabra (pal : xs) = palabra == pal || pertenece palabra xs
