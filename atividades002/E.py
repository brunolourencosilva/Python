#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:26/04/2024
#atividade 002 Letra E

import os 


os.system('cls')


print('-'*70)
print('sistema de cálculo de preços de passagens de ônibus')
print('='*70)

#entrada
distancia = float(input('INFORME A DISTANCIA DESEJADA: '))
resposta = ''
#processo
valor1 = distancia * 0.70
valor2 = distancia * 0.40

#condicional
if distancia < 200 and distancia == 200:
   resposta = f'SUA VIAGEM CUSTARA ${valor1}'
else:
    resposta = f'SUA VIAGEM CUSTARA ${valor2}'
 
#saida
print('-'*70)
print(f'SUA VIAGEM CUSTARA {resposta}')