# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 A-Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

import os


os.system('cls')

# Define a classe 'InicioFim' que irá armazenar os valores de início e final do intervalo
class InicioFim:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
        
# Define a classe Intervalo que herda atributos da classe InicioFim
class Intervalo(InicioFim):
    
    # Método para exibir os números dentro do intervalo
    def intervalo(self, inicio, final):
        
        contador = inicio
        
        # Usa um loop for para emprimir o intervalo
        for contador in range(inicio,final):
            print(f'{contador}', end=' | ')
            contador += 1

# Cria um objeto da classe Intervalo com o intervalo de 0 a 100
objeto_contador = Intervalo(0,100)
intervalo = objeto_contador.intervalo(0,100)
