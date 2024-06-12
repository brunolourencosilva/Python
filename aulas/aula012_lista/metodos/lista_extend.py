import os


os.system('cls')

# Inicializa alista vazia
lista_numeros = []

# Socilita ao usuario para inserir numeros separados por espaço
entrada = input('Digite numeros separados por espaço: ')

# Divide a string de entrada em uma lista de string
numeros = entrada.split()

# Cria uma lista para armazenar os numeros pares
pares = []

# Itera sobre os numeros inseridos
for numero in numeros:
    # Coverte a string para inteiro
    numeros_aux = int(numero)
    # Verificar se o numero é par
    if numeros_aux % 2 == 0:
        # Adicione o numero par na lista de pares
        pares.append(numeros_aux)
        
# Usa extend() para adicionar todos os numeros pares a lista principal
lista_numeros.extend(pares)

print(f'Numeros pares adicionados a lista: {lista_numeros}')