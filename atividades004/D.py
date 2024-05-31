# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:23/04/2024
# atividade004 D-Faça um programa que leia uma frase e depois exiba na tela:
# • A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.


import os


os.system('cls')

print('-'*70)
print('um programa que exiba na tela:')
print('A frase em minúsculas, a frase em maiúsculas,a quantidade\nde caracteres na frase e quantas letras tem a 2ª palavra na frase')
print('='*70)

# entrada
frase = 'Eu penso,logo eu sei'

# fatiamento
frase_fatiada = frase[:5]
# funções
maiuscula = frase.upper()
minuscula = frase.lower()
quantidade_caracteres = len(frase)
frase_fatiada_quantidade = len(frase_fatiada)

# saida
print('-'*70)
print(f'Frase em maiusculo: {maiuscula}')
print('.'*70)
print(f'Frase em minusculo: {minuscula}')
print('.'*70)
print(F'Quantidade de caracteres na 2ª palavra na frase : {frase_fatiada_quantidade}')
print('.'*70)
print(F'Quantidade de caracteres na frase: {quantidade_caracteres}')
print('='*70)