"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función
len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def contador(cadena):
    aux = 0
    for elemnto in cadena:
        aux += 1
    return print(aux)


if __name__ == "__main__":
    lista = "hola mundo"
    contador(lista)
