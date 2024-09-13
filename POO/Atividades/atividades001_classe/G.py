# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 G-Faça um programa que converta metros em centímetros e milímetros.

import os


os.system('cls')

class Calcular:
    def __init__(self,metros):
        self.metros = metros
    
    def convertor_centimetros(self,metros):
        centimetros = metros * 100
        return centimetros
    
    def convertor_milimetros(self,metros):
        milímetros = metros * 1000
        return milímetros

print('INFORME UM VALOR EM METROS')
metros = float(input('VALOR: '))

resultado = Calcular(metros)

centimetros = resultado.convertor_centimetros(metros)
milimetros = resultado.convertor_milimetros(metros)

print('-'*70)
print('RESULTADOS')
print('-'*70)
print(f'CENTIMETROS....: {centimetros}')
print(f'MILIMETROS.....: {milimetros}')