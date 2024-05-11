# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:10/05/2024
# atividade 003 Letra G

import os
import math


os.system('cls')

print('-'*70)
print('Programa que pega os valores a, b e c de uma equação do 2º grau')
print('='*70)

# entrada
a = int(input('INFORME O VALOR DA LETRA A: '))
b = int(input('INFORME O VALOR DA LETRA B: '))
c = int(input('INFORME O VALOR DA LETRA C: '))

# processo
delta = math.pow(b, 2) - (4 * a * c)

# condicional
if delta < 0:
    verificação = F'ERRO!!!,O DELTA DEU UM NUMERO NEGATIVO'
else:
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    x2 = (-b - (math.sqrt(delta))) / (2 * a)
    verificação = f'As raizes da equação é: x1:{x1}| x2:{x2}'
    
# saida
print(f'-'*70)
print(f'{verificação}')
print('='*70)