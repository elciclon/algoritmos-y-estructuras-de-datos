{-Implementar la función dineroEnStock :: [(String, Int)] ->[(String, Float)] ->Float
problema dineroEnStock (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : R {
requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
requiere: {Todo producto de stock aparece en la lista de precios}
asegura: {res es igual a la suma de los precios de todos los productos que est´an en stock multiplicado por la cantidad
de cada producto que hay en stock}
}
Para resolver este ejercicio pueden utilizar la funci´on del Preludio de Haskell fromIntegral que dado un valor de tipo
Int devuelve su equivalente de tipo Float.-}

dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float
dineroEnStock (producto:[]) precios = dineroEnProducto producto precios
dineroEnStock (producto : stock) precios = dineroEnProducto producto precios + dineroEnStock stock precios

dineroEnProducto :: (String, Int) -> [(String, Float)] -> Float
dineroEnProducto (prod, cantidad) ((item, precio) : precios)
  | prod == item = (fromIntegral cantidad) * precio
  | otherwise = dineroEnProducto (prod, cantidad) precios
