#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:26/04/2024
#atividade 002 Letra C

import os


os.system('cls')


print('-'*70)
print('sistema de monitoramento de velocidade')
print('='*70)

#entrada de dados
vel_carro = float(input('INSIRA A VELOCIDADE DO CARRO: '))
print('-'*70)

#declaração
vel_maxima = 60
resposta = ''


#condicional
if vel_carro > vel_maxima:
    resposta = (f'O CARRO ESTA ULTRAPASSANDO O LIMITE DE VELOCIDADE DE {vel_maxima}KM/H!!!') 
    
elif vel_carro == vel_maxima:
    resposta = (f'O CARRO ESTA COM NO LIMITE DE VELOCIDADE DE {vel_maxima}KM/H!!!')
    
else:
    resposta = (f'O CARRO ESTAR ABAIXO DO LIMITE DE VELOCIDADE DE {vel_maxima}KM/H')
    
#saida
print(resposta)
print('='*70)
print()