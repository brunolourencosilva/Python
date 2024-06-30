# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 E-Faça um programa para criar um dicionário com 5  ferramentas.
# Depois,  imprima os valores e a quantidade de elementos do dicionário.

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 5 ferramentas.')
print('-'*70)

# Declaração de dicionario
dicionario = {}

for i in range(5):
    print(f'Informe os dados da {i + 1}º ferramenta:')
    nome = str(input('Nome da ferramenta: '))
    descricao = str(input('Descrição da ferramenta: '))
    
    # Adiciona a ferramenta ao dicionário
    dicionario[nome] = descricao

print('-'*70)
print('Ferramentas adicionadas:')
print('-'*70)

# Imprime os valores dos elementos do dicionário
for nome, descricao in dicionario.items():
    print(f'Ferramenta: {nome}, Descrição: {descricao}')
    print('-'*70)

# Imprime a quantidade de elementos no dicionário
print(f'Quantidade de ferramentas adicionadas: {len(dicionario)}')
print('='*70)