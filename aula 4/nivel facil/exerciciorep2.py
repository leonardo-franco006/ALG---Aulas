num = int(input('Digite um número: '))
mult = 0

for i in range (1, 10 + 1):
    mult = num * i
    print(f'{num} x {i} = {mult}')