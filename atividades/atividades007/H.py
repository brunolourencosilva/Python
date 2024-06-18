# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade007 H-Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random


os.system('cls')

print('-'*70)
print('Programa que sorteia os números da Mega Sena e da Lotofácil')
print('='*70)
#criação de lista
mega_sena = []
lotofacil = []

for i in range(1,61): # criando numero de 1 a 60
    i = int(i)
    mega_sena.append(i)
    if i <= 25: 
        lotofacil.append(i) # pegando apenas os numeros abaixo de 25

mega = random.sample(mega_sena,6) # pegando apenas 6 numeros 
loto = random.sample(lotofacil,15)# pegando apenas 15 numeros

mega.sort()
loto.sort()

print(f'Numeros da mega cena: {mega}')
print(f'Numeros da lotofacil: {loto}')
print('-'*70)