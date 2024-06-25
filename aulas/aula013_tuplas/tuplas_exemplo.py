import os


os.system('cls')

# Solicitar o usuario a quantidade de elementos na tupla
numero_elementos = int(input('Quantos elementos na tupla?: '))

# Inicializar um lista vazia armazenar os elementos
elementos = []

# Estruturas de repetição para obter os elementos do usuario
for i in range(numero_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit(): # verifica se a entrada é um numero
            elementos.append(int(valor))
            break
        else:
            print('Entrada invalidade. Digite um numero.')

# Converte a lista para uma tupla
tupla = tuple(elementos)

print('-'*70)
# Exibir a tupla criada
print(f'Tupla criada: {tupla}')
print('-'*70)

# Estruturas de repetição para permitir multiplos
# Operações ate que o usuario deseja sair
while True:
    # Condicional para verificar a presença de
    # um numero especifico
    valor = int(input('Verificar se o numeros esta na tupla: '))
    
    if valor in tupla:
        print(f'O numero {valor} esta na tupla.')
        contagem = tupla.count(valor)
        print(f'O numero { valor} aparece {contagem} vez(es).')
        # Encontrando o indice da primeira ocorencia
        
        indice = tupla.index(valor)
        print(f'A 1° ocorencia de valor {valor} esta no indice {indice}')
    else:
        print(f'O numero {valor} não esta na tupla.')
    
    # Perguntar ao usuario se deseja realizar
    # outra operação ou sair
    continuar = input('Deseja continuar? (s/n): ').lower()
    if continuar != 's':
        print('Encerrando o programa. até mais!!!')
        break
print('-'*70)
print('Fim do programa!')
print()