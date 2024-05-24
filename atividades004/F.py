# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:23/04/2024
# atividade004 F-Faça um programa que receba o nome completo de uma pessoa e, posteriormente, imprima esse nome separadamente.

import os


os.system('cls')

print('-'*70)
print('Programa que receba o nome completo de uma pessoa ')
print('Posteriormente, imprima esse nome separadamente. ')
print('='*70)

#entrada
nome = str(input('Insira o seu nome: '))
#função strings
nome_separado = nome.split(' ')
primeiro_nome = nome_separado[0]
sobrenome = nome_separado[1]
sobrenome2 = nome_separado[2]
ultimo_nome = nome_separado[-1]

#saida
print('Nome separado:')
print(f'{primeiro_nome}')
print(f'{sobrenome}')
print(f'{sobrenome2}')
print(f'{ultimo_nome}')