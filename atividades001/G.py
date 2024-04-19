#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 G-Faça um programa que converta metros em centímetros e milímetros.

import os


os.system('cls')


print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('INFORME UM VALOR EM METROS')
metros = float(input('VALOR: '))

#processo
centimetros = metros * 100
milimetro = metros * 1000

#saida
print('-'*70)
print('RESULTADOS')
print('-'*70)
print(f'CENTIMETROS....: {centimetros}')
print(f'MILIMETROS.....: {milimetro}')