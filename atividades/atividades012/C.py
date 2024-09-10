# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 C-Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')


class InicioFim:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

class Intervalo_invertido(InicioFim):
    
    def intervalo(self, inicio, final):
        
        contador = inicio

        for contador in range(inicio,final + 1):
            print(f'{final}', end=' | ')
            final -= 1

print('-'*70)
print('Programa que imprima os números no intervalo entre 1 e 10 em ordem decrescente')
print('='*70) 


objeto_contador = Intervalo_invertido(0,10)
intervalo = objeto_contador.intervalo(0,10)
