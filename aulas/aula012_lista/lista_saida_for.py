import os


os.system('cls')

print('-'*70)
print('Saida com for')
print('='*70)

#Criando uma lista
lista_aluno = []

for c in range (0,5):
    nome = str(input('Entre com o nome do aluno: '))
    
    #guardando em uma lista
    lista_aluno.append(nome)

print()
print('Impressão dos nomes alunos: ')

#utilizando o len() para saber a quantidade de alunos
for aluno in range(len(lista_aluno)):
    print(lista_aluno[aluno],end=' ')
    if aluno == 3:       
        print()

print()
print('-'*70)
print('Fim do programa!')
print('-'*70)
