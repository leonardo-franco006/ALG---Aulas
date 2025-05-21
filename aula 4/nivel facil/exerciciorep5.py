num = int(input('Digite um número: '))
soma = 0

if num <= 0:
    print('O número precisa ser inteiro e positivo.')
else:
    for i in range (1, num + 1):
        if i % 2 != 0:
            soma += i
print('A soma é:', soma)