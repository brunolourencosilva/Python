# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:10/05/2024
# atividade 003 Letra F

import os 
import random


os.system('cls')

print('-'*70)
print('programa de adivinhar o número que o computador está ‘pensando’.')
print('='*70)

#entrada
numero = int(input('ESCREVA UM NUMERO ENTRE 1 A 10: '))

#processo
numero_aleatorio  = random.randint(1,10)

#condicional
if numero < 1 or numero > 10:
    verificação = f'O NUMERO NÃO ESTA ENTRE 1 E 10!!!'
else:
    verificação = f'NUMERO ACEITO'

if numero == numero_aleatorio:
    resposta = F'PARABENS VOCE ACERTOU, O NUMERO ERA {numero_aleatorio}'
else:
    resposta = f'QUE PENA VOCE ERROU,O NUMERO ERA {numero_aleatorio}'
    
#saida
print('-'*70)
print(f'{verificação}')
print('='*70)
print('RESULTADO')
print('.'*70)
print(f'{resposta}')
print('='*70)