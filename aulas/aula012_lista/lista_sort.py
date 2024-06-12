import os


os.system('cls')

#solicite ao usuario para inserir numeros separados por espaço
entrada = input('DIGITE NUMEROS SEPARADOS POR ESPAÇOS: ')

#Divide a string de entrada em uma lista de string
numeros_str = entrada.split

#converte a lista de string em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

#solicite ao usuario para inserir o numero que deseja encontrar na lista
busca_numero = int(input('Digite o numero que deseja encontrar: '))

#tente encontrar o indice do numero fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'O numero {busca_numero} esta no indice {indice}.')
else:
    print(f'O numero {busca_numero} não foi encontrado na lista.')

#exiba a lista fornecida para referencia
print(f'lista fornecida: {numeros}')
