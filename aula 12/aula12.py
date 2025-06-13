'''
map - transforma um iterato e devolve novo array
filter - aplica condição e devolve os itens que passaram na condicional 

REDUCE - APLICA UMA FUNÇÃO DE DOIS ARGUMENTOS 
CUMULATIVAMENTE AOS ITENS DE ITERÁVEL

-> reduzir o iterável a um único valor
[2, 3, 4, 5] => 3

SINTAXE
from functools import reduce
reduce(func, array)

'''
from functools import reduce
from random import randint

numeros = [randint(1, 50) for _ in range(10)]

soma_total = reduce(lambda x, y: x + y, numeros)

maior = reduce(lambda x, y: x if x > y else y, numeros)


print(numeros)
print(soma_total)
print(maior)
