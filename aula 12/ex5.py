# EXERCICIO 5 - encontrar a média dos números que são maiores que 5 após elevar ao quadrado
from functools import reduce
from random import randint

numeros = [randint(1, 10) for _ in range(10)]

media = reduce(lambda x, y: x + y, filter(lambda x: x > 5, map(lambda x: x * 2, numeros))) / len(list(filter(lambda x: x > 5, numeros)))

print(media)