
def func1(x, y):
    h = x ** func2(y)

def func2(x):
    u = func3(x, x*2, x*3) ** 0.5

def func3(a, b, c):
    lista = [x**2 for x in [a, b, c] if x % 3 == 0]
    return lista 


print(func1(2, 3))