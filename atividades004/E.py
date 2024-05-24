# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:23/04/2024
# atividade004 E-Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.

import os


os.system('cls')

print('-'*70)
print('Programa que receba uma frase e, em seguida,\nmostre quantas vezes as vogais foram utilizadas.')
print('='*70)

# entrada
frase = str(input('Digite uma frase: '))
print('.'*70)

# função count
quantida_vogais_a = frase.count('a')
quantida_vogais_e = frase.count('e')
quantida_vogais_i = frase.count('i')
quantida_vogais_o = frase.count('o')
quantida_vogais_u = frase.count('u')
# saida
print(f'quantidade de vogal "a": {quantida_vogais_a}')
print(f'Quantidade de vogal "e": {quantida_vogais_e}')
print(f'Quantidade de vogal "i": {quantida_vogais_i}')
print(f'Quantidade de vogal "o": {quantida_vogais_o}')
print(f'Quantidade de vogal "u": {quantida_vogais_u}')
