#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:26/04/2024
#atividade 002 Letra D


import os


os.system('cls')


print('-'*70)
print('sistema automatizado para calcular os aumentos salariais')
print('='*70)

#entrada de dados
salario_atual = float(input('INFORME O SALARIO DO FUNCIONARIO: '))
resposta = ''
print('-'*70)

#processo
aumento_1 = (5 / 100) * salario_atual
apos_aumento_1 = aumento_1 + salario_atual

aumento_2 = (10 / 100) * salario_atual
apos_aumento_2 = aumento_2 + salario_atual

#condicional
if salario_atual >= 1500.00:
    resposta = f'SALARIO APÓS AUMENTO DE 5%: {apos_aumento_1}'
elif salario_atual <= 1000.00:
    resposta = f'SALARIO APÓS AUMENTO DE 10%: {apos_aumento_2}'
else:
    resposta = f'O SALARIO {salario_atual} INFORMADO ESTA ERRADO'

#saida
print(f'{resposta}')
print('='*70)