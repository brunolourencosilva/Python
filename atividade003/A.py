# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:10/05/2024
# atividade 003 Letra A

import os
import math


os.system('cls')

print('-'*70)
print('Programa que recebe um valor e mostre sua raiz quadrada')
print('='*70)

# entrada
valor = int(input('Insira um valor: '))
print('.'*70)

# processamento
raizQuadrada = math.sqrt(valor)
#arredondar_para_cima = math.ceil(raizQuadrada)
##arredondar_para_baixo = math.floor(raizQuadrada)

#Condicional
<<<<<<< HEAD
if raizQuadrada :
    reposta = f'O VALOR {valor} É INVALIDO'
else:
    reposta = f'A raiz quadrada do valor {valor} é: {raizQuadrada}'

# saida
print(f'{reposta}')
#print(F'{arredondar_para_baixo}')
#print(f'{arredondar_para_cima}')
=======
 if raiz_quadrada % 1 == 0:
        resposta =  f'Raiz quadrada é exata'
    else:
        resposta =  f'Raiz quadrada não é exata'

# saida
print(f'{resposta}')
print(F'{arredondar_para_baixo}')
print(f'{arredondar_para_cima}')
>>>>>>> c5a64ce161700a51b780737d5bf0133a969f9a02
