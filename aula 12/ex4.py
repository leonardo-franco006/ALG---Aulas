# EXERCICIO 4 - calcular o produto dos números pares após multiplicar por 2
from functools import reduce
from random import randint

numeros = [randint(1, 10) for _ in range(10)]

produto = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numeros)))

print(produto)

# resolução do professor: produto = reduce(lambda x, y: x * y, map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))