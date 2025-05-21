idade = 10
pi = 3.14
nome = 'léo' 
status = True 

nota1 = input('Digite a nota 1 do aluno: ')

print('A nota digitada foi ', nota1)

# ler duas notas e efetuar as 4 operações mat. 

not1 = int(input ('Digite a nota 1 do aluno: ')) 
not2 = int(input('Digite a nota 2 do aluno: '))

print('Resultado da soma = ', not1 + not2)
print('Resultado da subtração = ', not1 - not2)
print('Resultado da divisão = ', not1 / not2)
print('Resultado da multiplicação = ', not1 * not2)

#ler as 4 notas de um aluno e calcular a media 
#mostrar a média no final 

n1 = float(input ('Digite a nota 1 do aluno: ')) 
n2 = float(input ('Digite a nota 2 do aluno: ')) 
n3 = float(input ('Digite a nota 3 do aluno: ')) 
n4 = float(input ('Digite a nota 4 do aluno: ')) 

media = (n1 + n2 + n3 + n4) / 4 
print('A média do aluno é: ', media)

#calcular a média ponderada tb, onde os pesos são:
# 0.2, 0.1, 0.4, 0.3

media_p = (n1 * 0.2 + n2 * 0.1 + n3 * 0.4 + n4 * 0.3)
print('Nota 1: ', n1, ' Nota 2: ', n2, ' Nota 3: ', n3, ' Nota 4: ', n4)
#f-strig
print(f'Nota 1: {n1}, Nota 2: {n2}, Nota 3: {n3}, Nota 4: {n4}')

print('Média ponderada = ', media_p)