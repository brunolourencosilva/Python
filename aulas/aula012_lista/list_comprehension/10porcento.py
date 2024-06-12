import os


os.system('cls')

print('-'*70)
print('ESTRUTURAS DE DADOS: LIST COMPREHENSION [ ]')
print('='*70)

lista_numeros = [100,200,300,400,500]

# triplicando os valores
lista_com_juros = []

for item in lista_numeros:
    
    lista_com_juros.append(item + (item * .10))

print('Aplicar 10% de juros: forma normal')
print(f'Lista triplicada: {lista_com_juros}')
print()

# List comprehension
lista_com_juros_2 = [item + (item * .10) for item in lista_numeros]
print('Aplicar 10% de juros: list comprehension')
print(f'Lista triplicada: {lista_com_juros_2}\n')