# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 K-Faça um programa que peça continuamente o nome e a idade de uma pessoa.
# Caso o usuário digite a idade 999, o programa será finalizado e executará uma impressão com os nomes cadastrados.

import os


# Declaração de dicionario
dicionario = {}
# Declaração de lista
lista = []

while True:
    os.system('cls')
    print('Esse é um programa que pedira\ncontinuamente o nome e a idade do usuario.')
    print('-'*70)
    nome = str(input('Nome: '))
    idade = int(input('Idade(999 para sair): '))
    print('-'*70)
        
    dicionario['Nome'] = nome# Adicionando nome ao dicionário
    dicionario['Idade'] = idade # Adicionando idade ao dicionario
    lista.append(dicionario.copy())# Adiciona uma cópia do dicionário de frutas à lista
    
    print('Dados adicionados!!')
    print(f'{dicionario}')
    input('\nPressione Enter para continuar...')
    os.system('cls')
    
    if idade == 999:
        break
    else:
        os.system('cls')
        
os.system('cls')
print('Nomes cadastrados:')
print('-'*70)
for dados in lista:
    print(dados['Nome'])
print('-'*70)

print('Fim do programa!!!')