# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 I-Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.

import os 


os.system('cls')

class Convertor:
    def __init__(self,real):
        self.real = real
        
    def real_pra_dolar(self,real):
        dolar = real / 5.65
        return dolar
    
print('-'*70)
print('INFORME UM VALOR EM REAIS')
print('-'*70)
real = float(input('VALOR:'))
resultado = Convertor(real)
moeda_convertida = resultado.real_pra_dolar(real)

print('-'*70)
print('RESULTADOS DE REAL PARA DOLAR')
print(f'DOLAR....: {moeda_convertida}')