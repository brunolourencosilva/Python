
import os


os.system('cls')

print('-'*70)
print('Faça um programa que leia o nome de uma pessoa')
print('='*70)

#entrada
nome = str(input('Digite o primeiro nome: '))
sobrenome = str(input('Digite o sobrenome: '))

#condicional
if "oliveira" in sobrenome:
    resposta = 'O sobrenome oliveira esta presente'
else:
    resposta = 'O sobrenome oliveira não esta presente'

#saida
print(f'{resposta}')