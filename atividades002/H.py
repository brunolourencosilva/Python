# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:29/04/2024
# atividade 002 Letra H

import os


os.system('cls')

print('-'*70)
print('Software de cálculo de raízes de equações quadráticas')
print('='*70)

# declação
a = 1
b = -6
c = 5
resposta = ''

# processo
delta = (b**2) - (4 * a * c)
x1 = (-b + delta ** (1/2)) / (2 * a)
x2 = (-b - delta ** (1/2)) / (2 * a)

# condicional
if delta < 0:
    resposta = f'OS CALCULOS DOS VALORES NÃO TERA UMA RAIZ REAL'
else:
    resposta = f'X1 = {x1} | X2 = {x2}'

# saida
print(f'{resposta}')
print('='*70)
print()
