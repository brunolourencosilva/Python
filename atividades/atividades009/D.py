# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 D-Faça um programa para criar um dicionário com 5 cores.
# Depois, imprima as chaves e os valores deste dicionário.

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 4 elementos.')
print('-'*70)

# Declaração de dicionario
dicionario = {}

for i in range(5):
    print(f'Informe os dados da {i + 1}º cor:')
    nome = str(input('Nome da cor: '))
    
    print('.'*70)
