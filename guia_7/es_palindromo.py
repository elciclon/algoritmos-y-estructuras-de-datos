def es_palindromo(s: str) -> bool:
    palindromo: str = ""
    for letra in s:
        palindromo = letra + palindromo
    if palindromo == s:
        return True
    else:
        return False
