import os
import math


os.system('cls')

print("-"*70)
print('ESTUDO DA BIBLIOTECA MATEMATICA MATH')
print('='*70)
print()

# entrada de dados
numero_decimal = float(input('Entre com um numero decimal: '))

#processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

#saida
print('-'*50)
print(f'O numero {numero_decimal} arredondar para cima é: {arredondar_para_cima}')
print(f'O numero {numero_decimal} arredondar para cima é: {arredondar_para_baixo}')
print('-'*50)