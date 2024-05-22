import os


os.system('cls')

print('-'*70)
print('Funções String')
print('='*70)

frase1 = 'Olá, mundo!'
quantidade_caracteres = len(frase1) # Conta os caracteres
print(f'A frase {frase1} \ncontém {quantidade_caracteres} caracteres')
print('.'*70)

minusculas = frase1.lower() # Frase em minusculo
print(f'Frase original: {frase1}')
print(f'Frase nova: {minusculas}')
print('.'*70)

maiusculas = frase1.upper() # Frtase em maiusculo
print(f'Frase original: {frase1}')
print(f'Frase nova: {maiusculas}')
print('.'*70)

captalizada = frase1.capitalize() # Frase capitalizada
print(f'Frase original: {frase1}')
print(f'Frase nova: {captalizada}')
print('.'*70)

frase2 = '   Ola mundo   '
sem_espaco = frase2.strip() # Retirar espaços, antes e depois
print(f'Frase original: {frase2}')
print(f'Frase nova: {sem_espaco}')
print('.'*70)

substituicao = frase1.replace("mundo", "Python") # Troca palavras
print(f'Frase original: {frase1}')
print(f'Frase nova: {substituicao}')
print('.'*70)

lista = frase1.split(',') # Separa as palavras de uma str em uma lista
print(f'Frase original: {frase1}')
print(f'Frase nova: {lista}')
print('.'*70)

lista = ['ola', 'mundo']
juncao = '-'.join(lista) # Transforma uma lista em uma string com separador
print(f'Frase original: {lista}')
print(f'Frase nova: {juncao}')
print('.'*70)