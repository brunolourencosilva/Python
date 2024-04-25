#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:24/04/2024
#estudo de condicional: parte 1
#objetivo: verificar um valor decimal

import os


os.system('cls')

print('_'*70)
print('ESTUDOS DE CONDICIONAL: PARTE 1')
print('='*70)

#entrada
valor = float(input('DIGITE UM NUMERO: '))
resposta = ''

#condicional
if valor % 1 == 0:
    valor = int(valor)
    resposta = f'ENTRADA INCORRETA, O VALOR {valor} É UM INTEIRO!'
else:
    resposta = f'ENTRADA CORRETA, O VALOR {valor} É UM DECIMAL!'
    
#saida
print('='*70)
print(resposta)

print('FIM DO PROGRAMA!\n') # \n salta uma linha
