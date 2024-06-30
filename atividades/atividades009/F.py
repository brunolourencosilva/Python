# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 F-Faça um programa que cadastra 5 tipos de vinho.
# Para os campos deste cadastro tome como referência nome do vinho, tipo, teor alcoólico e safra.

import os


os.system('cls')

print('='*70)
print('Programa que cadastra 5 tipos de vinho.')
print('-'*70)

# Declaração de dicionario
dicionario = {}
lista = []
while True:
    os.system('cls')
    print('-'*70)
    print('Adega de vinhos Château Lafite Rothschild.')
    print()
    print('Opções')
    print('1.Adicionar vinho')
    print('2.Mostrar os vinhos na adega')
    print('3.Sair')
    
    opcao = int(input('Escolha uma opção: '))
    print('-'*70)
    
    if opcao == 1: # Adicionar um novo vinho
        os.system('cls')
        print('-'*70)
        print(f'Informe os dados do vinho')
        nome = (input('Nome: '))
        tipo = (input('Tipo: '))
        teor = (input('Teor alcoolico: '))
        safra = int(input('Safra: '))
        print('.'*70)
        
        # Adicionando os dados ao dicionario
        dicionario['nome'] = nome
        dicionario['tipo'] = tipo
        dicionario['teor'] = teor
        dicionario['safra'] = safra
        
        lista.append(dicionario.copy())# Adicionando uma copia a lista
        
        print('Vinho adicionado!!')
        print(f'Informações do vinho: {dicionario}')
        input('\nPressione Enter para continuar...')
        os.system('cls')
    
    elif opcao == 2: #  Mostra os vinhos adicionados
        if dicionario:
            os.system('cls')
            print('-'*70)
            print('Vinho adicionados na adega:')
            print('-'*70)
            for vinho in lista:  # Itera sobre cada dicionário de vinho na lista 'lista'
                for chave, valor in vinho.items():
                    print(f'{chave}: {valor}') # Imprime a chave e o valor formatados
                print('-'*70)
            input('\nPressione Enter para continuar...')
        else:
            print('Adega vazia!!')
            input('\nPressione Enter para continuar...')
            os.system('cls')
    
    elif opcao == 3: # Encerra o programa
        print('-'*70)
        print('Fim do programa')
        print('Obrigado por escolher a adega Château Lafite Rothschild.')
        print('Tenha um bom dia')
        print('-'*70)
        break
    
    else:
        print('-'*70)
        print('Opção invalida!!!')
        print()
        input('\nPressione Enter para continuar...')
