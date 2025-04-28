{-Ejercicio 18. Implementar una función mayorDigitoPar :: Integer ->Integer segín la siguiente especificación:
problema mayorDigitoPar (n: N) : N {
requiere: { True }
asegura: { resultado es el mayor de los dígitos pares de n. Si n no tiene ningún dígito par, entonces resultado es -1.
}
}-}
iterador :: Integer -> Integer
iterador n | n <= 9 && mod n 2 /= 0 = -1