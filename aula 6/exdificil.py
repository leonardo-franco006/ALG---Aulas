'''
Exercício 4: Fatoração em Números Primos
Receba um número inteiro n maior que 1 e, utilizando apenas laços de repetição, apresente
sua fatoração em números primos.

Exemplo para n = 60:
2 * 2 * 3 * 5
'''

n = int(input('Digite um número inteiro maior que 1 para fatorar: '))

for i in range(2, n+1):
    while n % i == 0:
        print(i, end='*')
        n /= i
print()