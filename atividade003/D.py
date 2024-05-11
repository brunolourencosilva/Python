# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:10/05/2024
# atividade 003 Letra D

import os
import math


os.system('cls')

print('-'*70)
print('Programa que receba um ângulo qualquer')
print('='*70)

#entrada
angulo = float(input('INFORME UM VALOR DE ANGULO: '))

#processo
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
#saida
print(f'O seno do angulo {angulo} é.........: {seno:.2f}')
print(f'O cosseno do angulo {angulo} é......: {cosseno:.2f}')
print(f'A tangente fo angulo {angulo} é.....: {tangente:.2f}')