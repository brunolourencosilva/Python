#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 D-Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

print('-'*70)
print('Programa que imprime os números pares entre 0 e 100')
print('='*70) 

contador = 0 

while (contador <= 100):
    
    contador += 1 
    
    if (contador % 2 == 0): 
        print(f'numero par:{contador}')

print('-'*70)