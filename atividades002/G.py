#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:26/04/2024
#atividade 002 Letra G

import os


os.system('cls')

print('-'*70)
print('Programa para determinar se três segmentos podem formar um triângulo')
print('='*70)

#entrada de dados
a = float(input('DIGITE O 1º VALOR: '))
b = float(input('DIGITE O 2º VALOR: '))
c = float(input('DIGITE O 3º VALOR: '))
print('-'*70)
resposta = ''

#CONDICIONAL    
if (a + b) > c and (a + c) > b and (c + a) > b and (c + b) > a and ( b + a) > c and (b + c) > a:
    resposta = f'OS VALORES {a},{b} E {c} FORMAM UM TRIANGULO'
else:
    resposta = f'OS VALORES {a},{b} E {c} NÃO FORMAM UM TRIANGULO'

#saida
print(f'{resposta}')
print('='*70)