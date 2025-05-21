'''
1 - var de controle
2 - condição de parada 
3 - att da var de controle
'''
# 1 var de controle
i = 19
# 2 cond. de parada 
while i < 50:
    if i % 2 == 0:
        print(f'i = {i}')
        # 3 att da var 
    i = i + 1 # incremento 


# criar um laço de repetição com while que dependa da resposta do user p continuar o laço 
resp = 's'
while resp == 's':
    print('Ainda estou repetindo... ')
    while True:
        resp = input('Deseja continuar? (s) = sim / (n) = nao: ')
        resp = resp.lower() #.upper (maiuscula)
        if resp == 's' or resp == 'n':
            break
print('Terminei!!!')