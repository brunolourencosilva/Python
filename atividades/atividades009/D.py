# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 D-Faça um programa para criar um dicionário com 5 cores.
# Depois, imprima as chaves e os valores deste dicionário.

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 5 cores.')
print('-'*70)

# Declaração de dicionario
dicionario = {}
cores = []

for i in range(5):
    print(f'Informe os dados da {i + 1}º cor:')
    nome = str(input('Nome da cor: '))
    classificacao = str(input('Cor primaria,segundario ou terciaria?: '))
    dicionario[nome] = classificacao
    print('-'*70)
    cores.append(dicionario.copy())# Adicionando uma copia a lista

print('Cores Adicionadas:')
for cores in dicionario:
    for chave,valor in dicionario.items():
        print('-'*70)
        print(f'{chave}: {valor}')