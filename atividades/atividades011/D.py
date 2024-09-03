# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 D-Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.
import os


os.system('cls')

class Calcular:
    def __init__(self,dividendo ,divisor):
        self.dividendo = dividendo
        self.divisor = divisor
        
    def divisao(self,dividendo,divisor):
        quociente = dividendo / divisor
            
        return quociente

print('-'*70)
print('ENTRADA DE DADOS')
print('-'*70)

#entrada
print('-'*70)
print('INFORMER OS VALORES')
print('-'*70)
dividendo = float(input('DIVIDENDO....: '))
divisor = float(input('DIVISOR......: '))

quociente = Calcular(divisor,dividendo)
resultado = quociente.divisao(dividendo,divisor)

print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'ESSA DIVISÃO EM 4 CASA DECIMAIS: {resultado:.4f} ')