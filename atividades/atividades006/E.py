# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade006 E-Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

#não funiona direito!!!
import os


os.system('cls')

print('-'*70)
print('Programa que le vogais,e depois mostra em ordem inversa.')
print('='*70)

#entrada
frase = (input('Digite uma frase: '))
#separação da frase
frase_cortada = frase.split()
#criação da lista
lista_frase = []

for vogais in frase_cortada:
    lista_frase.append(str(vogais))

contagem = frase_cortada.count('a')
frase_revertida = lista_frase.reverse()


print(f'Quantidade de vogais que aparece: {contagem}')
print(f'Frase revertidade: {frase_revertida}')