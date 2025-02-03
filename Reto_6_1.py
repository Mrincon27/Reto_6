def operaciones(N1, N2, operador):
    if operador == "+":
        return N1 + N2
    elif operador == "-":
        return N1 - N2
    elif operador == "*":
        return N1 * N2
    elif operador == "/":
        if N2 == 0:
            return "Error: División por cero."
        return N1 / N2
    else:
        return "Error: Operador no válido."

try:
    N1 = float(input("Ingrese un numero: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    N2 = float(input("Ingrese el segundo numero: "))
    
    if not operador:
        print("Error: No se permiten entradas vacías para el operador.")
        exit()
    
    if operador not in ["+", "-", "*", "/"]:
        print("Error: Operador no válido.")
        exit()
    
    if operador == "/" and N2 == 0:
        print("Error: No se puede dividir por cero.")
        exit()
    
    resultado = operaciones(N1, N2, operador)
    print(f"El resultado de la operacion es: {resultado}")

except ValueError:
    print("Error: Debe ingresar un valor numérico")