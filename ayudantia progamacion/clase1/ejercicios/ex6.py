"""
 Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería
 devolver la cadena "odnaborp yotse"
"""


def inversa(cadena):
    largo = len(cadena)
    ultimo = cadena[largo - 1]
    ultimo2 = cadena[-1]

    for i in range(largo - 1, -1, -1):
        print(cadena[i], end="")
    return


if __name__ == "__main__":
    inversa([1,2,3,4,5])
