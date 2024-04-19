#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 H-Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.


import os 


os.system('cls')

print('-'*70)
print('entrada de dados')
print('-'*70)

#entrada
print('INFOMER UM VALOR INTEIRO')
print('-'*70)
valor = int(input('VALOR:'))

#processo
x1 = valor * 1
x2 = valor * 2
x3 = valor * 3
x4 = valor * 4
x5 = valor * 5
x6 = valor * 6
x7 = valor * 7
x8 = valor * 8 
x9 = valor * 9
x10 = valor * 10

#saida
print('-'*70)
print('TABUADA')
print('='*70)
print(f'{valor} X 1 = {x1}')
print(f'{valor} X 2 = {x2}')
print(F'{valor} X 3 = {x3}')
print(f'{valor} X 4 = {x4}')
print(f'{valor} X 5 = {x5}')
print(F'{valor} X 6 = {x6}')
print(f'{valor} X 7 = {x7}')
print(f'{valor} X 8 = {x8}')
print(F'{valor} X 9 = {x9}')
print(f'{valor} X 10 = {x10}')