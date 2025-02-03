def anagramas(lista):
    if not lista:
        print("Error: La lista de palabras no puede estar vacía.")
        return []

    if not all(palabra.isalpha() for palabra in lista):
        print("Advertencia: Algunas palabras contienen caracteres no alfabéticos.")

    lista = [palabra.lower() for palabra in lista]

    lista1 = {}
    for palabra in lista:
        clave = ''.join(sorted(palabra))
        if clave in lista1:
            lista1[clave].append(palabra)
        else:
            lista1[clave] = [palabra]

    resultado = []
    for grupo in lista1.values():
        if len(grupo) > 1:
            resultado.extend(grupo)

    return resultado

entrada = ["Amor", "roma", "mora", "corazon", "razonar"]
salida = anagramas(entrada)
print(salida)