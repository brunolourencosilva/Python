# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 A-Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

import os


os.system('cls')

class Contador:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
    def intervalo(self, inicio, final):
        
        contador = inicio
        
        while contador <= final:
            print(f'numero: {contador}', end=' | ')
            contador += 1

        return 

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

objeto_contador = Contador(inicio,final)

intervalo = objeto_contador.intervalo(inicio,final)

print('-'*70)