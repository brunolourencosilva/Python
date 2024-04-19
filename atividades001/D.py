#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 D-Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.

import os 


os.system('cls')


print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('-'*70)
print('INFORMER OS VALORES')
print('-'*70)
dividendo1 = float(input('DIVIDENDO....: '))
divisor1 = float(input('DIVISOR......: '))

#processo
quociente1 = dividendo1 / divisor1


#saida
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'ESSA DIVISÃO EM 4 CASA DECIMAIS: {quociente1:.4f} ')
