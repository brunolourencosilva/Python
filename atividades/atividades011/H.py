# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 H-Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.
import os 


os.system('cls')

class Calcular:
    def __init__(self,numero):
        self.numero = numero
        
    def mult(self,numero):
        for i in range(1,11):
            resultado = numero*i
            print(f"{numero} x {i} = {resultado}")
        
        return resultado

            
print('INFOMER UM VALOR INTEIRO')
print('-'*70)
numero = int(input('VALOR:'))

valor = Calcular(numero)
tabuada = valor.mult(numero)

