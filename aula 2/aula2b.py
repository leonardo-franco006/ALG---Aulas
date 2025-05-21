
'''
Atividade G:

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'Aluno aprovado com média {media}')
elif media >= 4: 
    print(f'Aluno em recuperação com média {media}')
else:
    print(f'Aluno reprovado com média {media}')
'''

# ler um número de 1 até 7 
# verificar a range 1 - 7 
# mostrar dia da semana, 1 - domingo ...

numero = int(input('Escolha um número de 1 - 7: '))

if numero >= 1 and numero <= 7:
    if numero == 1:
        print('Domingo')
    elif numero == 2:
        print('Segunda-feira')
    elif numero == 3:
        print('Terça-feira')
    elif numero == 4:
        print('Quarta-feira')
    elif numero == 5:
        print('Quinta-feira')
    elif numero == 6:
        print('Sexta-feira')
    else:
        print('Sábado')
else:
    print('Não existe dia na semana!')