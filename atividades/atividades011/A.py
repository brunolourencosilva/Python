# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:02/09/2024
# atividade0011 A-Faça um programa que peça 3 valores , depois calcule e imprima a soma e a multiplicação desses valores.

import os
os.system('cls')


class Calcular:
    def __init__(self, a, b, c):
        self.valor1 = a
        self.valor2 = b
        self.valor3 = c
        
    def soma(self, a, b, c):
        resultado_soma = a + b + c
        
        return resultado_soma
    
    def mult(self, a, b, c):
        resultado_mult = a * b *c
        
        return resultado_mult

print('-'*70)
print('ENTRADA DE DADOS')
print('='*70)

while True:
    print('-'*70)
    print('COLOQUE O VALORES DOS NUMEROS')
    a = float(input('COLOQUE O 1ª VALOR: '))
    b = float(input('COLOQUE O 2ª VALOR: '))
    c = float(input('COLOQUE O 3ª VALOR: '))
    print('-'*70)

    resultado = Calcular(a,b,c)

    escolha = input('Deseja somar ou multiplicar os numeros?: ')
        
    if escolha == 'somar':
        print(f'As somas dos numeros são {resultado.soma(a,b,c)}')
        input('Enter para continuar')
        os.system('cls')

    elif escolha == 'multiplicar':
        print(f'As somas dos numeros são {resultado.mult(a,b,c)}')
        input('Enter para continuar')
        os.system('cls')

    else:
        input('Opção inexistente!! Enter para continuar')
        os.system('cls')