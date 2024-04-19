#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 J-Faça um programa com entrada de dados para calcular o perímetro de um retângulo.

#importanto biblioteca
import os

#limpando o terminal
os.system('cls')

print('-'*70)
print('Entradas de dados')
print('-'*70)

#entrada
print('INFORME O VALORES DO RETÂNGULO')
print('-'*70)
altura = float(input('ALTURA....: '))
base = float(input('BASE......: '))

#processo
perimetro = (altura + base) * 2

#saida
print('-'*70)
print('RESULTADO')
print(f'PERÍMETRO: {perimetro}')