# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:23/04/2024
# atividade004 I-Faça um programa que receba o nome completo de uma pessoa e, em seguida, mostre o primeiro e o último nome.

import os


os.system('cls')

print('-'*70)
print('Faça um programa que receba o nome completo de uma pessoa')
print('e, em seguida, mostre o primeiro e o último nome.')
print('='*70)

# entrada
nome_completo = str(input('Digite o nome completo: '))

# função string
nome_separado = nome_completo.split(' ')
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]

# saida
print(f'Primeiro nome:{primeiro_nome}')
print(f'Ultimo nome:{ultimo_nome}')