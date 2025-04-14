bacterias :: Integer -> Integer -> Integer
bacterias poblacionInicial 1 = poblacionInicial * 2
bacterias poblacionInicial t = 2 * bacterias poblacionInicial (t - 1)