'''
EX 3 - crie um programa para ler o nome, a matricula e as 4 notas de 5 alunos 
e armazene em um dicionario = { matricula:nome, notas: [n1, n2, n3, n4] }
(as notas podem ser geradas de forma aleatoria com o uso de compreensão de listas)

alunos = {123: {'leo': [8, 9, 7, 8]}}

a) mostrar o aluno com maior media 
b) a % de alunos com media maior que 8
c) a % de alunos reprovados, considerando media < 4
'''

alunos = {}
import random

for i in range(2):
    matricula = int(input('Digite o número de matrícula: '))
    nome = input('Digite o nome do aluno: ')
    notas = [random.randint(0, 10) for _ in range(4)]
    alunos[matricula] = nome, notas

soma = sum(notas)

print(alunos)
print(soma)
