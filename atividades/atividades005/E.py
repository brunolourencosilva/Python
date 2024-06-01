#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:31/04/2024
#atividade005 E-Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

print('-'*70)
print('Programa que some a quantidade de números pares\nencontrados no intervalo entre 0 e 100.')
print('='*70) 

#declaração
contador = 0 
soma = 0

for contador in range(contador, 100):
    
    contador += 1
    if (contador % 2 == 0): 
        print(f'numero par:{contador}')
        soma += contador 

print('-'*70)
print(f'Soma dos pares: {soma}')
print('-'*70)