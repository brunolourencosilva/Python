#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:17/06/2024
#atividade006 B-Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

print('-'*70)
print('Uma lista com 5 números inteiros.\nQue depois imprime a soma desses valores.')
print('='*70) 

soma = 0
lista_numeros = [1,2,3,4,5,6]

for indice,numero in enumerate(lista_numeros):
    soma += numero 

print(f'Lista dos valores: {lista_numeros}')
print(f'Soma dos valores da lista: {soma}')
print('-'*70)
