#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 B-Faça um programa que peça o ano do seu nascimento e calcule a sua idade.


# importando biblioteca
import os

import datetime


os.system('cls')


print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('-'*70)
print('INFORME SUA IDADE')
idade = int(input('ANO DE NASCIMENTO: '))

#processo
ano_atual = datetime.datetime.now().year  #pegando a dada atual 
idade_atual = int(ano_atual) - idade      #fazendo o calculo para descobrir a idade

#saida
print('-'*70)
print('SAIDA DE DADOS')
print('-'*70)
print(f'VOCE TEM {idade_atual} ANOS DE IDADE!!!')