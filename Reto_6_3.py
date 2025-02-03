def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [num for num in lista if primo(num)]

try:
    entrada = input("Ingrese una lista de números separados por comas: ")
    
    if not entrada.strip():
        raise ValueError("Error: No se permiten entradas vacías.")

    try:
        numeros = [int(num.strip()) for num in entrada.split(",")]
    except ValueError:
        raise ValueError("Error: La lista debe contener solo números separados por comas.")
    
    if any(num < 0 for num in numeros):
        print("Advertencia: Los números negativos no son válidos para verificar si son primos.")

    primos = filtrar_primos(numeros)
    print(f"Los números primos en la lista {numeros} son: {primos}")

except ValueError as error:
    print(error)