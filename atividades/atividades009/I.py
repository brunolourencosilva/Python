# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 I-Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, delete o último elemento e mostre uma listagem nova.

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 4 elementos.')
print('-'*70)

# Declaração de dicionario
elementos = {}

# Declaração de lista
periodica = []

# Declaração
contagem = -1

while True:
    os.system('cls')
    
    print('Tabela periodica')
    print()
    print('Opções')
    print('1.Adicionar elemento')
    print('2.Remover elemento')
    print('3.Mostrar tabela periodica')
    print('4.Sair')
     
    opcao = int(input('Escolha uma opção: '))
    

    if opcao == 1: # entrada com os dados dos elementos
        os.system('cls')
        contagem += 1
        print('.'*70)
        print(f'Informe os dados do {contagem + 1}º elemento:')
        nome = str(input('Nome do elemento: '))
        simbolo = str(input('Simbolo do elemento: '))
        print('.'*70)
        
        elementos[nome] = simbolo
        periodica.append(elementos.copy())# Adicionando uma copia a lista
        
        print('Elemento adicionado!!')
        print(f'nome: {nome} | Simbolo: {simbolo}')
        input('\nPressione Enter para continuar...')
        print('.'*70)
        os.system('cls')
    
    elif opcao == 2: # Remover o ultimo elemento 
        if elementos:
            os.system('cls')
            print('.'*70)
            elemento_removido = elementos.popitem()
            
            print(f'Elemento removido: {nome}: {elemento_removido}')
            print('.'*70)
            input('\nPressione Enter para continuar...')
            print('.'*70)
            os.system('cls')
        else:
            print('Tabela vazia,por favor adicionar elementos nela!!')
            input('\nPressione Enter para continuar...')
            print('.'*70)
            os.system('cls')
        
    elif opcao == 3: # Mostrando a tabela periodica atual
        os.system('cls')
        if elementos:
            print('-'*70)
            print('Elementos adicionados: ')
            print('-'*70)
            # Imprimindo os elementos dentro do dicionario
            for chave, valor in elementos.items():
                print(f'{chave}: {valor}')
            print('-'*70)
                
            input('\nPressione Enter para continuar...')
            print('.'*70)
            os.system('cls')
        else:
            print('Tabela vazia,por favor adicionar elementos nela!!')
            input('\nPressione Enter para continuar...')
            print('.'*70)
            os.system('cls')
            
    elif opcao == 4: # Encerra o programa 
        os.system('cls')
        print('Elementos adicionados: ')
        print('-'*70)
        for chave, valor in elementos.items():
            print(f'{chave}: {valor}')
        print('-'*70)
        print('Fim do programa!!')
        print('-'*35)
        break
    else:
        print('Opção invalida!!')
        input('\nPressione Enter para continuar...')
        os.system('cls')
