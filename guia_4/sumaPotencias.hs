--req: True
--asegura: sumatoria de i=1 hasta n de sumatoria de j=1 hasta m q elevado a i + j
 
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias base 1 1 = base ^ 2
sumaPotencias base i j = sumatoriaInterior base i j + sumaPotencias base (i - 1) j

sumatoriaInterior :: Integer -> Integer -> Integer -> Integer
sumatoriaInterior base i 1 = base ^ (i + 1) 
sumatoriaInterior base i j = base ^ (i + j) + (sumatoriaInterior base i (j - 1))
