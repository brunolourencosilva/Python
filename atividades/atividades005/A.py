#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 Faça um programa que imprima os números no intervalo entre 1 e 100.
#Os números devem ser apresentados na horizontal.

import os


os.system('cls')

print('-'*70)
print('Programa que imprima os números no intervalo entre 1 e 100')
print('='*70) 

contador = 0
numero_final = 10

while contador <= 100:
    print(f'numero: {contador}', end=' | ')
    contador += 1