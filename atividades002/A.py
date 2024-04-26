#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:25/04/2024
#atividade 002 Letra A

import os 


os.system('cls')


print('-'*70)
print('VERIFICADOR DE IMPAR OU PAR')
print('='*70)

#ENTRADA
valor = int(input('DIGITE UM VALOR: '))
reposta = ''

#CONDICIONAL    
if valor % 2 == 0:
    resposta = f'O VALOR {valor} É PAR'
else:
    resposta = f'O VALOR {valor} É IMPAR'
    
#SAIDA
print('-'*70)
print(resposta)
print('-'*70)
print('FIM DO PROGRAMA!!\n')