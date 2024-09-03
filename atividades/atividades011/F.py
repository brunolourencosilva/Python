# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 F-Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.
import os


os.system('cls')

class Calcular:
    def __init__(self,numero):
        self.numero = numero
        
    def dobro(self,numero):
        resultado_dobrado = numero * 2
            
        return resultado_dobrado
    
    def triplo(self,numero):
        resultado_triplicado = numero * 3
        
        return resultado_triplicado
    
print('INFORME UM VALOR')
numero = float(input('valor:'))

resultado = Calcular(numero)

dobro = resultado.dobro(numero)
triplo = resultado.triplo(numero)

print('-'*70)
print('RESULTADO')
print('-'*70)
print(f'DOBRO....: {dobro}')
print(f'TRIPLO...: {triplo}')
