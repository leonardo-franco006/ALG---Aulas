# EXERCICIO 2 - encontrar o maior número ímpar após elevar ao cubo 
from functools import reduce
from random import randint

numeros = [randint(1, 10) for _ in range(10)]

maior = reduce(lambda x, y: x if x > y else y, filter(lambda x: x % 2 != 0, map(lambda x: x ** 3, numeros )))

print(maior)

# resolução professor: maior = max(filter(lambda x: x % 2 != 0, map(lambda x: x ** 3, numeros )))