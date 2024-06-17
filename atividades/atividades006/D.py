# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:17/06/2024
# atividade006 D-Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os


os.system('cls')

print('-'*70)
print('Programa que preenche uma lista com as notas de 4 alunos\nQue depois imprime a média.')
print('='*70)

#entrada
nota_1 = float(input('Coloque que a nota do 1º aluno: '))
nota_2 = float(input('Coloque que a nota do 2º aluno: '))
nota_3 = float(input('Coloque que a nota do 3º aluno: '))
nota_4 = float(input('Coloque que a nota do 4º aluno: '))
print('.'*70)

#criando lista pra notas
lista_notas= [nota_1,nota_2,nota_3,nota_4]

#processo
#somando as notas
soma_notas  = nota_1+nota_2+nota_3+nota_4
#descobrindo a media
media_notas = soma_notas / len(lista_notas)

#saida
print(f'Lista de notas dos alunos: {lista_notas}')
print(f'Media das notas: {media_notas}')
print('='*70)