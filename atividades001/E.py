#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 E-Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

import os 


os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

# entrada
print('INFORME UM VALOR')
numero = int(input('VALOR:'))

# processo
antecessor = numero - 1
sucessor = numero + 1

# saida
print('-'*70)
print('RESULTADO')
print(f'ANTECESSOR....: {antecessor}')
print(f'SUCESSOR......: {sucessor}')