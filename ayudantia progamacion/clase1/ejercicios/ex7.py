#calcular aproximacion de pi mediante las series de leibniz y nilakantha

def nilakantha(n):
    if n == -1:
        return float(3)
    else:
        return 4 * (pow(-1,n)/float(pow(2*n+3,3)-(2*n+3)))+nilakantha(n-1)


def nilakantha1(n):
    if n == -1:
        return float(3)
    else:
        pi = 0
        for i in range(n,0,-1):
            pi += 4*((-1**n)/(((2*n+3)**3)-(2*n+3)))
        return pi+nilakantha1(n-1)


def leibniz(n):
    result = 0.0
    sign = 1.0
    for n in range(n):
        result += sign / (2.0 * n + 1.0)
        sign = -sign
    return 4 * result



print(nilakantha(555))
print(nilakantha1(990))