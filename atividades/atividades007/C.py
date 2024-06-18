# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 C-Faça um programa que preencha uma lista com 50 números aleatórios.
# Depois fatie essa lista em 5 listas de 10 elementos.

import os
import random


os.system('cls')

print('-'*70)
print('Programa que preencha uma lista com 50 números aleatórios.\nDepois fatie essa lista em 5 listas de 10 elementos.')
print('='*70)
#declaração
soma = 0

numero_aleatorio = [random.randint(1, 100) for _ in range(50)] # Gerando um numero entre 1 e 100 mas usando apenas 50 dos numeros

print(f'lista de numeros aleatorios: {numero_aleatorio}')
print('.'*70)
print(f'lista 1: {numero_aleatorio[1:10]}')
print(f'lista 2: {numero_aleatorio[11:20]}')
print(f'lista 3: {numero_aleatorio[21:30]}')
print(f'lista 4: {numero_aleatorio[31:40]}')
print(f'lista 5: {numero_aleatorio[41:50]}')
print('-'*70)