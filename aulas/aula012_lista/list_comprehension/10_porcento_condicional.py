import os


os.system('cls')

print('-'*70)
print('ESTRUTURAS DE DADOS: LIST COMPREHENSION [ ]')
print('='*70)

lista_preços = [100,200,300,400,500]

# triplicando os valores
lista_com_juros = []

for valor in lista_preços:
    if valor < 300:
        lista_com_juros.append(valor + (valor * .10))

print('Aplicar 10% de juros: forma normal')
print(f'Lista triplicada: {lista_com_juros}')
print()

# List comprehension
lista_com_juros_2 = [valor+ (valor * .10) for valor in lista_preços if valor < 300]
print('Aplicar 10% de juros: list comprehension')
print(f'Lista triplicada: {lista_com_juros_2}\n')