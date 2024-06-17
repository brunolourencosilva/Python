# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade006 F-Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os


os.system('cls')

print('-'*70)
print('Programa que le 5 nomes,e depois imprime estes nomes\ncom seus respectivos índices.')
print('='*70)

#Criação da lista
nome_lista = []

#Entrada
for i in range(5):
    nome = input(f'Digite o nome {i+1}: ')
    nome_lista.append(nome)

#Exibindo a lista de nomes inseridos
print('Lista de nomes:', nome_lista)

#Solicitando ao usuário para verificar se um nome está na lista
while True:
    print('.'*70)
    nome_verificar = input('Digite qual nome queres ver: ')
    print('.'*70)
    if nome_verificar in nome_lista:
        indice = nome_lista.index(nome_verificar)
        print(f'O nome "{nome_verificar}" está na posição {indice} da lista.')
    else:
        print(f'O nome "{nome_verificar}" não está na lista.')
        print('='*70)