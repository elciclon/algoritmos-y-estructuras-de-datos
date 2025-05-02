{-Implementar la funci´on aplicarOferta :: [(String, Int)] ->[(String, Float)] ->[(String,Float)]
problema aplicarOferta (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : seq⟨String × R⟩ {
requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
requiere: {Todo producto de stock aparece en la lista de precios}
asegura: {|res| = |precios|}
asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) > 10, entonces res[i]0 = precios[i]0 y
res[i]1 = precios[i]1∗ 0,80}
asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) ≤ 10, entonces res[i]0 = precios[i]0 y
res[i]1 = precios[i]1 }
}-}
aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta stock ((item, precio) : [])
  | pertenece item (filtrarProductos stock) == True = [(item, precio * 0.8)]
  | otherwise = [(item, precio)]
aplicarOferta stock ((item, precio) : precios)
  | pertenece item (filtrarProductos stock) == True = (item, precio * 0.8) : aplicarOferta stock precios
  | otherwise = (item, precio) : aplicarOferta stock precios

filtrarProductos :: [(String, Int)] -> [String]
filtrarProductos ((producto, cantidad) : [])
  | cantidad > 10 = [producto]
  | otherwise = []
filtrarProductos ((producto, cantidad) : stock)
  | cantidad > 10 = producto : filtrarProductos stock
  | otherwise = filtrarProductos stock

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece palabra (pal : xs) = palabra == pal || pertenece palabra xs
