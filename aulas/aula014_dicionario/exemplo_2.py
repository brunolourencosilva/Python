import os


os.system('cls')
print('-'*70)
print('------ TABELA PERIODICA ------ ')
print('='*70)

# Inicialização do dicionario e da lista
elemento = {} # Dicionario
periodica = [] # lista

while True:
    os.system('cls')
    
    # Cabeçalho do menu
    print('-'*70)
    print('MENU DE OPÇÕES')
    print('='*70)
    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')
    
    # Solicitação da escolha
    opcao = input('Escolha uma opção (1-5):')
    
    if opcao == '1':
        # Adicionar um elemento
        simbolo = str(input('Simbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elemento['Simbolo'] = simbolo
        elemento['nome'] = nome
        periodica.append(elemento.copy())
        input('\nElemento adicionado. Pressinoe Enter para continuar...')
    
    elif opcao == '2':
        # Visualizar todos os elementos
        print('\nElemento na tabela periodica:')
        print('-'*70)
        for elemento in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.capitalize()}: {valor}')
            print('-'*70)
        input('\nPressione Enter para continuar...')
    
    elif opcao == '3':
        # Atualizar um elemento
        simbolo = str(input('Digite o simbolo do elemento para atualizar: '))
        # Inicializa a flag como false
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'Digite o novo simbolo para'
                f' {simbolo} (ou deixar em branco para manter o atual): '))
                novo_nome = str(input(f'Digite o novo nome para'
                f' {simbolo} (ou deixar em branco para manter o atual): '))
                
                # Atualizar o simbolo e o nome se fornecidos
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag como true quando o elemento é encontrado
                encontrado = True
                break
        
        if encontrado:
            input('\nElemento atualizado. Enter para continuar...')
            input('\nElemento não encontrado. Enter para continuar...')
    
    elif opcao == '4':
        # Remover um elemento
        simbolo = str(
            input('Digite o simbolo do elemento que deseja remover: '))
        encontrado = False # inicializa a flag como false
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                # Define a flag como true quando o elemento é encontrado
                encontrado = True
                break
        if encontrado:
            input('\nElemento removido. Enter para continuar...')
        else:
            input('\nElemento não encontrada. Enter para continuar...')
    
    elif opcao == '5':
        print('Saindo do programa.')
    
    else:
        input('Opção invalida. Enter para tentar novamente...')