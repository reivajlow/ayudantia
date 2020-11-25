#4- Escribir una función que tome un carácter y devuelva True si es
# una vocal, de lo contrario devuelve False.

def vocal(caracter):
    resultado = bool()
    if caracter in "aeiouAEIOUáéíóú":
        resultado = True
    else:
        resultado = False

    return print(resultado)


if __name__ == "__main__":
    vocal(input("ingrese caracter: "))
