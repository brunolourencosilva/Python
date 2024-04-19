#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 F-Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.

#importanto biblioteca
import os 

#limpando o terminal
os.system('cls')


print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('INFORME UM VALOR')
valor = float(input('valor:'))

#processo
dobro = valor * 2
triplo = valor * 3

#saida
print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'DOBRO....: {dobro}')
print(f'TRIPLO...: {triplo}')
