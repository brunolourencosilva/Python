# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 A-Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

import os


os.system('cls')

class InicioFim:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

class Intervalo(InicioFim):
    
    def intervalo(self, inicio, final):
        
        contador = inicio

        for contador in range(final + 1):
            print(f'{contador}', end=' | ')
            contador += 1


objeto_contador = Intervalo(0,100)
intervalo = objeto_contador.intervalo(0,100)

print('-'*70)