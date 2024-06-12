import os


os.system('cls')

print('-'*70)
print('ESTRUTURAS DE DADOS: LIST COMPREHENSION [ ]')
print('='*70)

lista_numeros = [1,2,3,4,5]

# triplicando os valores
lista_nova_triplicando = []

for item in lista_numeros:
    lista_nova_triplicando.append(item * 3)
    
print('Triplicar os valores: forma normal')
print(f'Lista triplicada: {lista_nova_triplicando}')
print()

#list comprehensions
lista_nova_triplicando_2 = [item * 3 for item in lista_numeros]
print('Triplicar os valores: lista comprehension')
print(f'Lista trplicada: {lista_nova_triplicando_2}\n')