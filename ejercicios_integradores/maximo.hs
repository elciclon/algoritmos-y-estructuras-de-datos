import Test.HUnit

{-Implementar la funci´on maximo :: Tablero ->Int
problema maximo (t: Tablero) : Z {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
asegura: {res es igual al n´umero m´as grande del tablero t}
}-}

type Fila = [Int]

type Tablero = [Fila]

-- maximo :: Tablero -> Int

maximoLocal :: [Int] -> Int
maximoLocal (x : y : [])
  | x > y = x
  | otherwise = y
maximoLocal (x : y : xs)
  | x > y = maximoLocal (x : xs)
  | otherwise = maximoLocal (y : xs)

separarFilas :: Tablero -> Fila
separarFilas tablero = head tablero

testSuiteMaximoLocal =
  test
    [ "maximoDeUnaLista" ~: (maximoLocal [3, 7, 5, 1, 8, 9, 23, 4, 78, 2]) ~?= 78
    ]

testSuiteSepararFilas = test ["desarmaTablero" ~: (separarFilas [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) ~?= [1, 2, 3]]

allTests :: Test
allTests =
  test
    [ testSuiteMaximoLocal,
      testSuiteSepararFilas
    ]

correrTests = runTestTT allTests