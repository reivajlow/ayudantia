# 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una
# lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lista):
    suma = 0
    for i in lista:
        if type(i) == float or type(i) == int:
            suma += i
        elif type(i) == str:
            try:
                suma += float(i)
            except:
                pass
    return print(suma)


def mult(lista):
    resu = 1
    for i in lista:
        if type(i) == float or type(i) == int:
            resu = resu * i
        elif type(i) == str:
            try:
                resu = resu * float(i)
            except:
                pass
    return print(resu)

x = [1,2,3,4,3.4233,"2","rr"]

mult(x)
