#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:3/06/2024
#atividade005 F-Faça um programa que imprima os números primos entre 0 e 100.

import os


os.system('cls')


print('-'*70)
print('Programa que imprime os números primos entre 0 e 100.')
print('='*70)

#declaração
inicio = 2
fim = 100
contador = inicio

for numero_primo in range(contador, fim):
    for divisor in range(2, int(numero_primo**0.5) + 1):
        if numero_primo % divisor == 0:
            break
    else:
        print(f'{numero_primo}')

print('-'*70)