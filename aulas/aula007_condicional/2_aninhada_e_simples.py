#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:25/04/2024
#estudo de condicional: parte 2
#objetivo: pratica com condicionais simples e aninhadas

import os 


os.system ("cls")


#declaração
a = 10
b = 5
resposta = ''

print('-'*70)
print('ESTUDOS DE CONDICIONAIS (SIMPLES)')
print('='*70)

#condicionais
if a > b:
    resposta = f'{a} É MAIOR QUE {b}'
else:
    resposta = f'{a} NÃO É MAIOR QUE {b}'

#saida
print('-'*70)
print(resposta)

#declaração
a = 5
b = 5

print('-'*70)
print('ESTUDOS DE CONDICIONAL (ANINHADA)')
print('='*70)

if a > b:
    resposta = f'{a} É MAIOR QUE {b}'
elif a < b:
    resposta = f'{a} É MENOR QUE {b}'
else:
    resposta = f'O VALORES SÃO IGUAIS: {a} = {b}'

#saida
print('-'*70)
print(resposta)
print('-'*70)
print()