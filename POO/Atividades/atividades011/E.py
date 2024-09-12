# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 E-Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.

import os


os.system('cls')


class Calcular:
    def __init__(self, numero):
        self.numero = numero
        
    def sucessor(self,numero):
        sucessor = numero + 1
        
        return sucessor
    
    def antecessor(self,numero):
        adjacentes = numero - 1
        
        return adjacentes

# entrada
print('INFORME UM VALOR')
numero = int(input('VALOR: '))

resultado = Calcular(numero)

antecessor = resultado.antecessor(numero)
sucessor = resultado.sucessor(numero)

print('-'*70)
print('RESULTADO')
print(f'ANTECESSOR....: {antecessor}')
print(f'SUCESSOR......: {sucessor}')
        