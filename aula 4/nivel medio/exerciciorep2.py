'''
Exercício 2: Número Perfeito
Faça um programa usando apenas laços que determine se um número informado pelo
usuário é um número perfeito. Um número é perfeito quando é igual à soma dos seus
divisores próprios (exceto ele mesmo).
Exemplo:
Entrada:
6

Saída:
Número Perfeito

Explicação: 6 → divisores: 1, 2, 3 (soma: 1+2+3=6)
'''
num = int(input('Digite um número: '))
soma = 0 

for i in range(1, num):
    if num % i == 0:
        soma += i
    elif soma == num:
        print('Número Perfeito.')
        break
else:
    print('Número Imperfeito.')