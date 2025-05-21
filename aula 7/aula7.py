'''
LISTAS / TUPLAS / DIC.

Listas -> coleções heterogêneas de objetos, podem ser qualquer tipo, inclusive outras listas 

[0, 1, 10, "beto", [0.2, 0.3]]

listas são mutávei, 

colchetes determinam uma lista []

todo indice começa em 0

// VETOR ?? EXISTE ?? -> VECTOR -> COLEÇÃO -> vetor

'''

lista = [1, 2, 3, 4, 5]

print(lista)

nome = 'beto'

print(nome[3])

#len -> função que retorna o tamanho de uma coleção
print(len(nome))

progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP', 'Metalica', 'U2']

progs[3] = 'Metalica' #alterando itens na lista

# 1 forma

for i in range(len(progs)): #len --> utilizado para o caso da lista crescer
    print(progs[i])

# 2 forma 

for prog in progs:
    print(prog)

# incluir novo elemento / Append object to the end of the list.
progs.append('Guns')

# trocar o ultimo elemento
progs[-1] = 'Novo elemento na ultima posição'

# ordenar 
progs.sort()

# inverter a lista
progs.reverse()

'''
--PESQUISA-- 

-> POP

-> REMOVE

-> ZIP

--PESQUISA--

-> set

-> frozenset
'''

for i, p in enumerate(progs): # i = indice , p = elemento 
    print(f'Posição {i} e elemento igual = {p} ')

# // função enumerate() retorna uma tupla de dois elementos a cada interação

# Dada as seguintes listas [A, B, C] e [D, E, F] como poderíamos juntar?

''' pensando em listas de 50 alunos, onde serão lidas (random) 4 notas (0 - 100) mostre:
    a % de alunos aprovados 
    a % de alunos reprovados 

    imprima os 5 primeiros alunos com a média mais alta 
    imprima os 5 piores alunos 
    imprima a nota mais alta, a posição e qual aluno pertence.

'''

# Tuplas --> semelhantes as listas, porém são imutáveis: mão acrescentar, apagar, fazer atribuições

tupla = (1, 2, 3, 4)

t1 = (1,)

print(tupla[0])


for t in tupla:
    print(t)

lista = list(tupla) # contrario utiliza: tuple

lista_tupla = ([1, 2, 3] , [2, 3], ('leonardo', 'luisa', 'marcelo', 'emilly'))

# união, interseção e diferença 

# o que é range? (pesquisa)