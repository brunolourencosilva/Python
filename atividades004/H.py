# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:23/04/2024
# atividade004 H-Faça um programa que leia o nome de um aluno e mostre quantas vezes 
# a letra 'o' aparece e em que posição ela aparece pela primeira e última vez.

import os


os.system('cls')

print('-'*70)
print('um programa que leia o nome de um aluno'
      +'\ne mostre quantas vezes a letra "o" aparece.')
print('='*70)

#entrada
nome = str(input('Insira um nome: '))

#função count
quantida_vogais_o = nome.count('o')
primeira_posição = nome.find('o')
ultima_posição = nome.rfind('o')
#saida
print(f'Quantidade de vezes que a letra "o" aparece: {quantida_vogais_o}')
print(f'Primeira posição da letra "o"..............: {primeira_posição}')
print(f'Ultima posição da letra "o"................: {ultima_posição}')
print('='*70)