# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:10/05/2024
# atividade 003 Letra B

import os
import math


os.system('cls')

print('-'*70)
print('Programa que receba 2 valores, faça a divisão entre eles')
print('='*70)

#entrada
valor1 = int(input('Informe o 1ª valor: '))
valor2 = int(input('Informe o 2ª valor: '))

#processo
resultado = valor1 / valor2

#condicional
if valor2 == 0:
    resposta = f'Os valores informados não podem ser divididos entre si!!'
elif valor1 % valor2 == 0:
    resposta = f'A divisão entre {valor1} e {valor2} é: {resultado}'
else:
    arredondar_cima = math.ceil(resultado)
    arredondar_baixo = math.floor(resultado)
    resposta = f'O resultado teve que ser arredondado: Para baixo:{arredondar_baixo}| Para cima: {arredondar_cima}|'
#saida
print('-'*70)
print(f'{resposta}')
print('='*70)
