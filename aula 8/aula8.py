'''
Dicionários 
- é uma lista de associações compostas por uma chave "única"
- são mutáveis 

sintaxe:
dicionario = {'a':1, 'b':2} // 'chave':'valor'

'''

dic = {'nome1':'leo', 'nome2': 'luisa', 'nome3':'emily'}

dic['nota'] = 7.80

# usando esse print para debug
print(dic)

# dic = {(1, 2, 3):'leonardo'} --> pode!

items = dic.items()
chaves = dic.keys()
valores = dic.values() 

print(f'Items = {items}')
print(f'chaves = {chaves}')
print(f'valores = {valores}')

#get ---> busca valores 

print(dic.get('nome1'))

# ------------------------------ 

for i, j in dic.items():
    print(f'i = {i}, j = {j}')

'''
1. leia o nome de 5 pessoas e armazene em um dicionario

2. crie um programa para gerar um dicionario com 20 numeros inteiros, 
mostre a soma de todos os elementos 

'''

# EX 1:
nomes = {}

for i in range(1):
    nom = input(f'Digite o {i+1}º nome: ')
    nomes[i] = nom 

print(nomes)


# EX 2:
from random import randint
num = {}

for i in range(20):
    num[i] = randint(1, 50)

soma = sum(num.values())
print(f'A soma dos numeros do dicionario = {soma}')

#compreensão de listas
lista = [i for i in range(5)] # --> [0, 1, 2, 3, 4]
print(lista)

# PESQUISA: como trabalhar com compreensão de listas 

# lista2 = [x, y for in range(3) for y in range(6) if x == y: x += 2]

