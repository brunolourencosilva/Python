# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 D-Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor
import os
import random


os.system('cls')

print('-'*70)
print('O mesmo exercício anterior,porem todas as listas\nestão em ordem crescente de valor')
print('='*70)

#declaração
soma = 0

numero_aleatorio = [random.randint(1, 100) for _ in range(50)]# Gerando um numero entre 1 e 100 mas usando apenas 50 dos numeros
numero_aleatorio.sort() # colocando os numeros gerados em ordem crescente
print(f'lista de numeros aleatorios: {numero_aleatorio}')
print('.'*70)
print(f'lista 1: {numero_aleatorio[1:10]}')
print(f'lista 2: {numero_aleatorio[11:20]}')
print(f'lista 3: {numero_aleatorio[21:30]}')
print(f'lista 4: {numero_aleatorio[31:40]}')
print(f'lista 5: {numero_aleatorio[41:50]}')
print('-'*70)