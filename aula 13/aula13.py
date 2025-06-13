'''
recursividade é uma tecnica de programação onde uma função chama a "si mesma" para resolver algum problema 

principais caracteristicas 
1 - caso base: condição de parada que evita chamadas infinitas 
2 - caso recursivo: onde a função chama a si mesma com um problema menor

'''

def func(x):

    # caso base:
    if x < 1:
        return 0
    print(x)
    return x + func(x - 1)

'''
3 + func(2)
2 + func(1)
1 + func(0)
'''

# --------------

print(func(3))

# FATORIAL 5:

def func2(x):

    if x == 1:
        return 1
    return x * func2(x - 1)
    
print(f'Fatorial de 5! = 5 x 4 x 3 x 2 x 1 = {func2(5)}')

# Fibonacci 7 = 1 1 2 3 5 8 13

def func3(x):
    if x <= 1:
        return x
    return func3(x - 1) + func3(x - 2)

fibo = [func3(i) for i in range(1, 8)]
print('Fibonacci de 7: ', fibo)


# EX 1 -> Inverter String: Crie uma função recursiva que inverta uma string 

# EX 2 -> Potencia: implemente uma função recursiva que calcule a ^ b, onde a e b são inteiros e b >= 0
