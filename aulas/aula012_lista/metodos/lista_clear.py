import os


os.system('cls')

#solicite ao usuario para inserir numeros separados por espaço
entrada = input('Digite numeros separados por espaços: ')

#Divide a string de entrada em uma lista de string
numeros_str = entrada.split()

#Converte a lista de string em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#solicita ao usuario para decidir se deseja limpar a lista
escolha = input("Deseja limpa a lista? (s/n): ").strip().lower()

#verifica a escolha do usuario e limpa a lista se a reposta for 's'
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')

#exibe a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')
