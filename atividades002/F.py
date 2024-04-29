#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:29/04/2024
#atividade 002 Letra F


import os


os.system('cls')

print('-'*70)
print('software de verificação de anos bissextos')
print('='*70)

#entrada de dados
ano = int(input('INFORME UM ANO: '))
resposta = ''

#condicional
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):   #fazendo os calculos de acordo com o calendário gregoriano
    resposta = f'O ANO {ano} É BISSEXTO'
else:
    resposta = f'O ANO {ano} NÃO É BISSEXTO'
    
#saida
print('-'*70)
print(f'{resposta}')
print('='*70)
print()
