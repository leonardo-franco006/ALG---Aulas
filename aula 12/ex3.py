# EXERCICIO 3 - somar os quadrados dos números que são múltiplos de 3
from functools import reduce
from random import randint

numeros = [randint(1, 10) for _ in range(10)]

soma = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numeros)))
print(soma)