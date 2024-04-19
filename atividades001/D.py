#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 D-Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

# AINDA EM PROCESSO DE DESENVOLVIMENTO!!!!!!!!

import os 


os.system('cls')


print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('-'*70)
print('INFORMER OS VALORES')
print('-'*70)
dividendo = float(input('DIVIDENDO....:'))
divisor = float(input('DIVISOR....:'))

#processo
quociente = dividendo / divisor

#saida
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A DIVISÃO ENTRE OS VALORES {dividendo} E {divisor} É IGUAL A: {quociente} ')

