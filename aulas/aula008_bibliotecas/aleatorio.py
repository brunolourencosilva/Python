import os
import random


os.system('cls')

print('-'*70)
print('Biblioteca random')
print('='*70)

#Gerdor de numeros aleatorios 
print('numero aleatorio')
numero_aleatorio = random.random()
print(f'O numero gerado foi: {numero_aleatorio:.3f}')
print('.'*70)

#Gerador de numero aleatorios inteiros
print('Numero aleatorio inteiro')
aleatorio_inteiro = random.randint(1,20)
print(f'O numero inteiro gerado foi: {aleatorio_inteiro}')
print('.'*70)

#Gerador de numeros aleatorios decimais 
print('Numero aleatorio decimal no intervalo')
aleatorio_decimal = random.uniform(1,10)
print(f'O numero decimal gerado foi: {aleatorio_decimal:.3f}')
print('.'*70)

print('Sorteio em uma lista')
lista = ['Agata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('.'*70)

print('Embaralhar sequencia')
lista2 = ['Agata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista2}')
#embaralha = list(random.shuffle(lista)) dá erro!!!
#embaralha = random.shuffle(lista) saida vazia!!!
random.shuffle(lista2)
print(f'Lista nova: {lista2}')
print('.'*70)

print('Retorno de elementos unicos de uma população')
numero = [1,2,3,4,5,6,7]
amostra_aleatoria = random.sample(numero, 5)
print(f'Retorno da amostragem: {amostra_aleatoria}')
print('.'*70)