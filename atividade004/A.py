#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:23/04/2024
#atividade004 A-Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa.
#Em seguida, imprima o nome completo.

import os 


os.system('cls')

print('-'*70)
print('Programa que solicite separadamente o nome')
print('='*70)

#entrada de dados
nome = str(input('Informe o primeiro nome: '))
sobrenome = str(input('Informe o sobrenome: '))
ultimo_nome = str(input('Informe o ultimo nome: '))

nome_completo = nome + sobrenome + ultimo_nome
lista = nome_completo.split('-')
print(f'Seu nome completo é {lista}')