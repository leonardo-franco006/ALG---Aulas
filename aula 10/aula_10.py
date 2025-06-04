import random
'''
gere 100 num rand (20 a 100), filtrar > 60
gere 100 num rand (20 a 100), filtrar > media
gere 100 num rand (20 a 100), filtrar < 25
'''

nums = [random.randint(20, 100) for _ in range(100)]

maiores = list(filter(lambda x: x > 60, nums))

print(maiores)

nums = [random.randint(20, 100) for _ in range(100)]

menores = list(filter(lambda x: x < 25, nums))

print(menores)
