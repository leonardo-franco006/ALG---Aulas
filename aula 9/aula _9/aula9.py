lista = [1, 2, 3, 4, 5]
quadrado = [num**2 for num in lista]
pares = [x for x in lista if x % 2 == 0]
print(quadrado)
print(pares)

# codigo aloca a função
def soma(num1, num2):
    # resultado = num1 + num2  --> variaveis de escopo local 
    return num1 + num2
# chamada da função:
retornoSoma = soma(2, 3)
print(retornoSoma)

def subtracao(num1, num2):
    return num1 - num2

retornoSub = subtracao(5, 3)
print(retornoSub)

def divisao(num1, num2):
    if num2 > 0:
        return num1 / num2
    print('Num2 - não pode ser 0')
retornoDiv = divisao(10, 0)
print(retornoDiv)

def multiplicacao(num1, num2):
    return num1 * num2

retornoMult = multiplicacao(5, 5)
print(retornoMult)

