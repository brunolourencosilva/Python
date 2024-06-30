# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 A-Faça um programa para criar um dicionário com 4 elementos.

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 4 elementos.')
print('-'*70)

elementos = {}
periodica = []

print('Tabela periodica')
print()

for i in range(4):
    print(f'Informe os dados do {i + 1}º elemento:')
    nome = str(input('Nome do elemento: '))
    simbolo = str(input('Simbolo do elemento: '))
    print('.'*70)
    
    elementos['nome'] = nome  # Adiciona o nome do elemento ao dicionário
    elementos['simbolo'] = simbolo   # Adiciona o símbolo do elemento ao dicionário

    periodica.append(elementos.copy())  # Adiciona uma cópia do dicionário 'elementos' à lista 'periodica

# Imprimindo os elementos adicionados
print('-'*70)    
print('Elementos adicionados: ')   
for elementos in periodica:
    for chave,valor in elementos.items():
        print(f'{chave}: {valor}')
    print('-'*70)