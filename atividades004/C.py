#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:23/04/2024
#atividade004 C-Faça um programa que leia o nome de uma pessoa
#e verifique se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.
import os


os.system('cls')

print('-'*70)
print('Faça um programa que leia o nome de uma pessoa')
print('='*70)

#entrada
nome = str(input('Digite o primeiro nome: '))
sobrenome = str(input('Digite o sobrenome: '))

#condicional
if "oliveira" in sobrenome or nome:
    resposta = 'O sobrenome oliveira esta presente'
else:
    resposta = 'O sobrenome oliveira não esta presente'

#saida
print(f'{resposta}')