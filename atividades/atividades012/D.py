# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 D-Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

class Intervalo:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
class Pares(Intervalo):
    def descobrir_par(self,inicio, final):
        
        contador = inicio
        
        for contador in range(final + 1):
            contador += 1 
            
            if (contador % 2 == 0): 
                print(f'{contador}', end= ' | ')


resultados = Pares(0,100)
numeros_pares = resultados.descobrir_par(0,100)