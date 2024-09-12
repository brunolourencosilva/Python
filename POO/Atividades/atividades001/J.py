# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 J-Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
import os
import math


os.system('cls')

class Calcular:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base
        
    def calculo_perimetro(self,altura,base):
        perimetro = 2 * (altura + base)
        
        return perimetro

print('INFORME O VALORES DO RETÂNGULO')
print('-'*70)
altura = float(input('ALTURA....: '))
base = float(input('BASE......: '))

resultado = Calcular(altura,base)
perimetro = resultado.calculo_perimetro(altura,base)

print('-'*70)
print('RESULTADO')
print(f'PERÍMETRO: {perimetro}')