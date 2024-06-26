import os


os.system('cls')

print('-'*70)
print('ESTRUTURAS DE DADOS:DICIONARIO') # dict => {}
print('='*70)

# Indice iguais: só iraa exibir um item.
dicionario1 = {'Nomes': 'John', 'nome': 'jane'}

# Posso ter uma tupla como indice e uma lista como valor
dicionario2 = {(1,2) : [1,2]}

# Mas não posso ter uma lista como indice e uma tupla como valor
dicionario3 = {[1,2] : (1,2)}

# Saida
print('-'*70)
print(dicionario1)
print(dicionario2)

print()