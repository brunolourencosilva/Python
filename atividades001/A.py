#curso de desenvolvimento de sistema
#autor:Bruno Lourenço
#data:19/04/2024
#atividade001 A-Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores.


#importação da biblioteca 
import os

# importando biblioteca
os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS')
print('='*70)


#entrada
print('-'*70)
print('COLOQUE O VALORES DOS NUMEROS')
valor1 = float(input('COLOQUE O 1ª VALOR: '))
valor2 = float(input('COLOQUE O 2ª VALOR: '))
valor3 = float(input('COLOQUE O 3ª VALOR: '))
print('-'*70)

#processo dos valores
soma = valor1 + valor2 + valor3
produto = valor1 * valor2 * valor3 

#saida
print('-'*70)
print('RESULTADOS')
print('-'*70)
print(f'A SOMA DOS VALORES {valor1} + {valor2} + {valor3} É IGUAL A: {soma}')
print(f'A MULTIPLICAÇÃO DOS VALORES {valor1} X {valor2} X {valor3} É IGUAL A: {produto} ')