import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print('\n Menu de opções:')
    print('1. Adicionar um par chave-valor')
    print('2. Mostra chaves do dicionario')
    print('3. Mostrar valores do dicionario')
    print('4. Mostrar itens do dicionario')
    print('5. Sair')
    print('-'*70)
    
    opcao = input('Escolha uma opção (1-5): ')
    
    if opcao == '1':
        #Adicionar um par chave-valor ao dicionario
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado.')
        
    elif opcao == '2':
        #Mostra as chaves do dicionario usando keys()
        if meu_dicionario:
            print('Chaves do dicionario:', meu_dicionario.keys())
        else:
            print('O dicionario esta vazio. Adicione item primeiro.')
    elif opcao == '3':
        #Mostra os valores do diciomnario usando value()
        if meu_dicionario:
            print('Valores do dicionario:', meu_dicionario.values())
        else:
            print('O dicionario esta vazio. Adicione itens primeiro.')
        
    elif opcao == '4':
        # Mostrando os itens (chave-valor) do dicionario usando items()
        if meu_dicionario:
            print('Itens do dicionario:', meu_dicionario.items())
        else:
            print('O dicionario esta vazio. Adicione itens primeiro.')
    
    elif opcao == '5':
        #Sai do programa
        print('Saindo do programa.')
        break
    else:
        #Mensagem para opção invalida
        print('Opção invalida. Tente novamente.')