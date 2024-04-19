#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 I-Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

#importanto biblioteca
import os 

#limpando o terminal
os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('-'*70)
print('INFORME UM VALOR EM REAIS')
print('-'*70)
real = float(input('VALOR:'))

#processo
dolar = real * 0.19 

#saida
print('-'*70)
print('RESULTADOS DE REAL PARA DOLAR')
print(f'DOLAR....: {dolar}')