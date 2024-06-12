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

#exiba a lista fornecida para referencia
print('listaista fornecida:',numeros)

#solicite ao usuario para decidir se deseja inverte a lista
escolha = input('deseja inverte a ordem da lista? (s/n): ').strip().lower()

#verifica a escolha do usuario e inverte a lista se  a resposta é s ou n
if escolha == 's':
    numeros.reverse()
    print('Lista invertida:',numeros)
else:
    print('A lista não foi invertida.')
