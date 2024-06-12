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

#solicite ao usuario para decidir se deseja
#criar uma copia da lista
escolha = input('Deseja criar unma copia? (s/n): ').strip().lower()

#verifica a escolha do usuario e cria uma copia da
#lista se a resposta for 's'
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f'Copia da lista: {lista_copiada}')
else:
    print('A lista não foi copiada.')

#exiba alista fornecida apra referencia
print(f'Lista fornecida: {numeros}')
