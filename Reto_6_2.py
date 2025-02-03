def palindromo(palabra):
    palabra = palabra.lower()
    longitud_p = len(palabra)

    for i in range(longitud_p // 2):
        if palabra[i] != palabra[longitud_p - 1 - i]:
            return False
    return True

try:
    palabra = input("Ingrese una palabra para verificar si es palíndromo: ")

    if not palabra.strip():
        raise ValueError("Error: No se permiten entradas vacías.")


    if not palabra.isalpha():
        raise ValueError("Error: Solo se permiten letras del alfabeto.")

    if len(palabra) == 1:
        raise ValueError("Error: Ingrese una palabra con más de un carácter.")

    es_palindromo = palindromo(palabra)
    print(f"La palabra '{palabra}' {'es' if es_palindromo else 'no es'} un palíndromo.")

except ValueError as error:
    print(error)