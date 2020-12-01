"""
defina una funcion que calcule el factorial de un numero
"""


def factorial(n):
    resultado = 1
    if n > 1:
        resultado = n * factorial(n - 1)
    return resultado


def cuenta(n):
    n -= 1
    if n > 0:
        print(n)
        cuenta(n)
    else:
        print("FIN")


cuenta(990)
