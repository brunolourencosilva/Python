import os


os.system('cls')

# Inicializando uma ista de exemplo
lista_numeros = [10,20,30,40,50,60,70,80,90,100]

# Solicite ao usuario para inserir um indice para remover o elemento
indice = int(input('Digite o indice de elemento  aser removido (0-9): '))

# verificar se o indice esta dentro do intervalo valido da lista
if 0 <= indice < len(lista_numeros):
    # Remove o elemento no indice especificado e exibe-o
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('indice invalido')
#exiba a lista resultando
print('Lista apos remoção: ',lista_numeros)