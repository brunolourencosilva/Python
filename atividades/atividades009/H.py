# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 H-Faça um programa para ler o dicionário nomes = 
# {‘nome’: ’John, ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}.
# Em seguida realize as seguintes ações:
# Listar chaves e valores com laço - Deletar o peso
# Listar novamente chaves e valores - mostrar o nome e altura

import os


os.system('cls')

print('='*70)
print('Programa que cadastra alunos de uma escola.')
print('-'*70)

# Declaração de dicionario
dicionario = {'nome': 'John', 'idade': '40', 'peso': '80', 'altura': '1.70'}

print('Chaves e valores do Dicionário:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
print('-'*70)

# Deletar a chave 'peso'
del dicionario['peso']

print('Chaves e valores após deletar "peso":')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')
print('-'*70)

# Mostrar o nome e altura
print(f'Nome: {dicionario["nome"]}, Altura: {dicionario["altura"]}')