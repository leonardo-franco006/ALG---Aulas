# EXERCICIO 1 - calcular a media dos quadrados dos numeros pares de uma lista 
from functools import reduce
from random import randint 


numeros = [randint(1, 50) for _ in range(10)]

media = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))


print(media)