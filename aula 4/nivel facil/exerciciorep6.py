num = int(input('Digite um número: '))
fat = 0

for i in range (1, num + 1):
    fat += num * i 
print(f'Fatorial é: {fat}')