import os 


os.system('cls')

#solicite ao usuario para inserir numeros separados por espaço
entrada = input('Digite numeros separados por espaços: ')

#Divide a string de entrada em uma lista de string
numeros_str = entrada.split()

#converte a lista de string em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#converte a lista de string em uma lista de inteiros
numeros_para_contar = int(input('digite o numero que deseja contar: '))

#conta o numero de vezes que o numero fornecido aparece na lista
contagem = numeros.count(numeros_para_contar)

if contagem > 0:
    print(f'O numero {numeros_para_contar} aparece {contagem} vezes na lista.')
else:
    print(f'O numero {numeros_para_contar} não aparece na lista.')

#Exiba a lista fornecida para referencia
print(f'Lista fornecida: {numeros}')
