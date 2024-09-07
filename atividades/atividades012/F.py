# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 F-Faça um programa que imprima os números primos entre 0 e 100.

import os


os.system('cls')

class Intervalo:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
class Primos(Intervalo):
    def descobrir_par(self,inicio, final):
        
        inicio = 3
        fim = 100
        contador = inicio
        
        for numero_primo in range(contador, fim):
            for divisor in range(2, int(numero_primo**0.5) + 1):
                if numero_primo % divisor == 0:
                    break
            else:
                print(f'{numero_primo}', end=" | ")
 


resultados = Primos(0,100)
numeros_impares = resultados.descobrir_par(0,100)