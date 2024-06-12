import os


os.system('cls')

print('-'*70)
print('Saida com for enumerate()')
print('='*70)

soma = 0

#Criando uma lista
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

#pecorrendo a lista com o enumerate()
#o comando enumerate adiciona um indice
#para cada valor de nosso lista
#start opcional, para não começar no indice 0
#enumerate(lista_numeros, start = 1)

#para cada numero dentro da lista de numeros,enumare com um indice
for indice, numero in enumerate(lista_numeros):
    soma += numero #soma os numeros
    print(f'indice: {indice} = numero: {numero}')

print('-'*70)
print(f'a soma de todos os numeros é: {soma}')
print('fim do programa')
print('-'*70)
