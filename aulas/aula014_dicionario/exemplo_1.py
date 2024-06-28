import os


os.system('cls')

# Inicialização do dicionario e da lista
elemento = {} # Dicionario
periodica = [] # lista

# Entrada de dados
for c in range(2): # Considerando a entrada de 2 elemento
    print(f'Entrada de dados {c + 1}:')
    simbolo = str(input('Simbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # Adicione os dados ao dicionario
    elemento['simbolo'] = simbolo
    elemento['nome'] = nome
    
    # Usando append() com copy() para adicionar uma copia do dicionario a lista
    periodica.append(elemento.copy())
    
print()
print('-'*70)
print('Elemento na tabela periodica:')
print('-'*70)
print()

# For aninhada para pecorrer a lista e o dicionario
print('Detalhes do elemento:')
for elemento in periodica: # Para cada elemento no lista
    for chave, valor in elemento.items(): # Para cada chave e valor do dicionario
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legivel
    print('-'*70) # Linha separadora entre elementos
    