import os


os.system('cls')

# Criação do dicionario vazio
meu_dicionario = {}

while True:
    print('-'*70)
    # Exibição do menu de opções
    print('\nMenu de opções')
    print('1. Adicionar um par chave-valor')
    print('2. Mostra o dicionario')
    print('3. Mostra o tamanho do dicionario')
    print('4. Fazer uma copia do dicionario')
    print('5. Limpar o dicionario')
    print('6. Sair')
    print('-'*70)
    
    # Solicitação da escolha do usuario
    opção = input('Escolha uma opção (1-6): ')
    
    if opção == '1':
        # Adicione um novo par chave-valor ao dicionario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave} : {valor} adicionado.')
    
    elif opção == '2':
        # Exibe o dicionario atual
        print('Dicionario atual:', meu_dicionario)
    
    elif opção == '3':
        # Mostra o tamanho do dicionario usando len()
        tamanho = len(meu_dicionario)
        print(f'O dicionario tem {tamanho} elemento.')
    
    elif opção == '4':
        #crie uma copia do dicionario usando copy() e exibe a copia
        copia_dicionario = meu_dicionario.copy()
        print('Copia do dicionario:', copia_dicionario)
    
    elif opção == '5':
        # Limpao dicionario usando clear()
        meu_dicionario.clear()
        
    elif opção == '6':
        # sai do programa
        print('Saindo do programa.')
        break
    
    else:
        # Mensagem para opção invalidade
        print('Opção invalida. Tente novamente.')