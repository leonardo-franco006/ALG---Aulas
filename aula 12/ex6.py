# EXERCICIO 6 - calcular a soma dos cubos dos números que são menores que a média da lista
from functools import reduce
from random import randint

numeros = [randint(1, 10) for _ in range(10)]