"""
 Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python
tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def maximo(num1,num2):
    if num1 > num2:
        print("el numero ",num1,"es mayor que ",num2)
    elif num1 < num2:
        print("el numero ", num2, "es mayor que ", num1)
    else:
        print("ambos numeros son iguales")
    return

"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def maximo2(lista):
    max = lista[0]
    for numero in range(1,len(lista)):
        if max < lista[numero]:
            max = lista[numero]
    return print(max)


def maximo3(lista):
    print(lista)
    lista.sort()
    print(lista)
    return print(lista[-1])




if __name__ == "__main__":
    a = [2,43,5,-12,33,2,24]
    maximo2(a)
