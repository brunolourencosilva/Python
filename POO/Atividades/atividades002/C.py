# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:06/09/2024
# atividade0012 C-Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')

# Define a classe InicioFim que irá armazenar os valores de início e final do intervalo
class InicioFim:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

# Define a classe Intervalo_invertido que herda atributos da classe InicioFim
class Intervalo_invertido(InicioFim):
    
    # Método para exibir os números dentro do intervalo na ordem decrescente
    def intervalo(self, inicio, final):
        
        contador = inicio

        for contador in range(inicio,final + 1):
            print(f'{final}', end=' | ')
            final -= 1

print('-'*70)
print('Programa que imprima os números no intervalo entre 1 e 10 em ordem decrescente')
print('='*70) 

# Cria um objeto da classe Intervalo_invertido pegando os valores de inicio e final
objeto_contador = Intervalo_invertido(0,10)
intervalo = objeto_contador.intervalo(0,10)
