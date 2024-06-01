#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 B-Evolua o programa anterior para um código que pergunte ao 
#usuário qual o intervalo que ele deseja ver  impresso.

import os


os.system('cls')

print('-'*70)
print('Programa anterior porem com input')
print('='*70) 

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

contador = inicio

while contador <= final:
    print(f'numero: {contador}', end=' | ')
    contador += 1

print('-'*70)