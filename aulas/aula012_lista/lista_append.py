import os


os.system('cls')

# Inicializa uma lista vazia
lista_numeros = []

# Pede ao usuario para inserir tres numeros
for i in range(3):
    numero = int(input('DIGITE UM NUMERO: '))
    
    # Adiciona o numero á lista
    lista_numeros.append(numero)
    
# Verifica se o numero inserido esta na lista e 
# exibe uma mensagem correspondente
numero_verificar = int(input("DIGITE UM NUMERO: "))

if numero_verificar in lista_numeros:
    print(f'O numero {numero_verificar} esta na lista!')
else:
    print(f'O numero {numero_verificar} não esta na lista.')