# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:23/04/2024
# atividade004 G-Faça um programa que receba um número inteiro e mostre na tela:
#• A quantidade de unidades, a quantidade de dezenas, a quantidade de centenas e a quantidade de milhares.

import os


os.system('cls')

print('-'*70)
print('Programa que receba um número inteiro e mostre na tela')
print('Quantidade de unidades,dezenas,centenas e de milhares.')
print('='*70)

#entrada
numero = int(input('Insira um numero: '))

#condicional de validação
if numero < 0:
    resposta = 'Numero negativo não é permitido'
    print(f'{resposta}')
    print('='*70)
else:
    #processamento
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhares = (numero // 1000) % 10
    #saida
    print(f'Unidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
    print(f'Milhares: {milhares}')
    print('='*70)