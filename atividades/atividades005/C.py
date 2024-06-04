#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 C-Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')

print('-'*70)
print('Programa que imprima os números no intervalo entre 1 e 10 em ordem decrescente')
print('='*70) 

#entrada
inicio = 1
fim = 10
contador = inicio

while contador <= fim:
    print(f'numero: {fim}')
    fim -= 1