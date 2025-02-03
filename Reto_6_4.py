def mayor_suma(lista):
    mayor_suma = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual
    return mayor_suma

try:
    entrada = input("Ingrese una lista de números separados por comas: ")

    if not entrada.strip():
        raise ValueError("Error: No se permiten entradas vacías.")

    try:
        numeros = [int(num.strip()) for num in entrada.split(",")]
    except ValueError:
        raise ValueError("Error: La lista debe contener solo números separados por comas.")

    if len(numeros) < 2:
        raise ValueError("Error: La lista debe contener al menos dos números.")

    resultado = mayor_suma(numeros)
    print(f"La mayor suma de dos números consecutivos en la lista {numeros} es: {resultado}")

except ValueError as error:
    print(error)