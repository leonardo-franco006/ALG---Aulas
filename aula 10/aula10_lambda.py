import random
import math
'''
Lambda function - usadas de forma rápida com corpo pequeno 

sintaxe: 
lambda argumentos: expressão 

'''

dobro = lambda x: x * 2

print('Exemplo 1 - dobro de 5:', dobro(5))

soma = lambda x, y: x + y 

print('Exemplo 2 - soma de 3 e 4:', soma(3, 4))


# calcular hipotenusa: 
hip = lambda cat1, cat2: (cat1 ** 2 + cat2 ** 2) ** 0.5 

print('A hipotenusa é: ', hip(3, 4))

# ou

hip = lambda cat1, cat2: math.sqrt(cat1 ** 2 + cat2 ** 2) 

print('A hipotenusa é: ', hip(3, 4))

# filter, map

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros)) # parametros (func , array)

print('Exemplo 3 - números pares: ', pares)


'''
gere 100 num rand (20 a 100), filtrar > 60
gere 100 num rand (20 a 100), filtrar > media
gere 100 num rand (20 a 100), filtrar < 25
'''
# nums = [random.randint(0, 10) for _ in range(20, 101)]


quadrado = list(map(lambda x: x ** 2, numeros)) # parametros (func , array)

print('Exemplo 4 (map) - números ao quadrado: ', quadrado)


# sorted(pessoas, key = lambda x: x[1])
pessoas = [('Ana', 19), ('João', 30), ('Maria', 20)]