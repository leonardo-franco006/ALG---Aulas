'''
1 - ler dois números onde o 1 vai ser o inicio do laço e o 2 o final.
validar os números de entrada.

num1 = int(input('Digite o inicio do laco: '))
num2 = int(input('Digite o final do laco: '))

if num1 > num2:
    for i in range(num2, num1):
        print(i)
else:
    for i in range(num1, num2):
        print(i)

2 - faça um triangulo retangulo com asteriscos 
1
11
111
1111
11111

3 - 
11111
1111
111
11
1

4 - ler um mes e um ano qualquer, exibir o calendario completo com os dias da semana
'''
#1:

for i in range(1, 6):
    for j in range(1, i):
        print(j, end = ' ')
    print('')

