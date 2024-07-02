# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 J-Faça um programa para criar um dicionário com nomes de frutas.
# Em seguida verifique se tem abacaxi nos valores.

import os


os.system('cls')

print('='*70)
print('Programa que cria um dicionário com 4 elementos.')
print('-'*70)

# Declaração de dicionario
dicionario = {}
lista = []
# Declaração
contagem = -1

while True:
    os.system('cls')
    
    print('Lista para frutas')
    print()
    print('Opções')
    print('1.Adicionar fruta')
    print('2.Mostrar lista de frutas')
    print('3.Sair')
     
    opcao = int(input('Escolha uma opção: '))
    

    if opcao == 1: # entrada com os dados das frutas
        os.system('cls')
        contagem += 1
        print('.'*70)
        print(f'Informe o nome da {contagem + 1}º fruta:')
        nome = str(input('Nome da fruta: '))
        print('.'*70)
        
        dicionario['Nome'] = nome# Adiciona a fruta ao dicionário
        lista.append(dicionario.copy())# Adiciona uma cópia do dicionário de frutas à lista
        
        print('Fruta adicionada!!')
        if 'abacaxi' in lista:
                print('Tem abacaxi na lista!!')
        else:
            print('Não a abacaxi na lista')
        
        print(f'nome: {nome}')
        input('\nPressione Enter para continuar...')
        print('.'*70)
        os.system('cls')
    
    elif opcao == 2: # Mostrar lista de frutas
        if dicionario:
            os.system('cls')
            print('-'*70)
            print('Frutas adicionados: ')
            print('-'*70)
            
            # Imprimindo as frutas dentro do dicionario
            for chave, valor in dicionario.items():
                print(f'{chave}: {valor}')
            print('-'*70)
                
            input('\nPressione Enter para continuar...')
            print('.'*70)
            os.system('cls')
        else:
            print('Lista vazia,por favor adicionar frutas nela!!')
            input('\nPressione Enter para continuar...')
            os.system('cls')
    
    elif opcao == 3: # Encerra o programa
        os.system('cls')
        print('Frutas adicionados: ')
        print('-'*70)
        for chave, valor in dicionario.items():
            print(f'{chave}: {valor}')
        print('-'*70)
        print('Fim do programa!!')
        print('-'*35)
        break
    else:
        print('Opção invalida!!')
        input('\nPressione Enter para continuar...')
        os.system('cls')