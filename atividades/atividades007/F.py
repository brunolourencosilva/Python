# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 F-Faça um programa que recebe 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares. 
import os


os.system('cls')

print('-'*70)
print('Programa que recebe 7 números inteiros.E depois quebre essa lista em:\nlista de pares e lista de ímpares. ')
print('='*70)
#criando lista
lista_numero = []
par = []
impar = []

#entrada
numeros_inteiros = input('Digite 7 numeros inteiros separados: ')
numero = numeros_inteiros.split()
lista_numero.extend(numero)

for num in lista_numero:
    num = int(num)
    
    if num % 2 == 0:#verificando se o numero é par
        par.append(num)
    else:
        impar.append(num)
        
print(f"Numeros pares:{par}")
print(f"Numeros impares:{impar}")