import os


os.system('cls')

# Lista original
lista = [1,2,3,4]

# Pedindo ao usuario para fornecer a
# posição e o elemento a se inserido
posicao = int(input('Posição onde deseja inserir o elemento: '))
elemento = int(input('Elemento a ser inserido: '))

# Verificando se a posição fornecida pelo usuario é valida
if posicao >= 0 and posicao <= len(lista):
    # Inserindo o elemento na lista especificada pelo usuario
    lista.insert(posicao,elemento)
    print('Lista apos a inserção:', lista)
else:
    print(f'Posição fora do intervalo 0, {len(lista)}')