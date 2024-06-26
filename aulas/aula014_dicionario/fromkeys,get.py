import os


os.system('cls')

meu_dicionario = None

# Loop principal do programa
while True:
    print('-'*70)
    print('\nMenu de opções:')
    print('1. Criar dicionario com fromkeys()')
    print('2. Buscar valor de uma com get()')
    print('3. Sair')
    print('-'*70)
    
    opcao = input('Escolha uma opção (1-3): ')
    
    if opcao == '1':
        # Criação de um dicionario usando fromkey()
        chaves = input('Digite as chaves separadas por virgulas: ').split(',')
        valor_padrão = input('Digite o valor padrão para as chaves: ')
        meu_dicionario = dict.fromkeys(chaves, valor_padrão)
        print('Dicionario criado:', meu_dicionario)
    
    elif opcao == '2':
        # Vifica se o dicionario foi criado antes de tentar acessa-lo
        if meu_dicionario is not None:
            chaves = input('Digite a chave que deseja buscar: ')
            valor = meu_dicionario.get(chaves, 'Chaves não encontrada')
            print(f'Valor para a chave "{chaves}": {valor}')
        else:
            print('Erro!!crie um dicionario.')
    elif opcao == '3':
        print('Saindo do programa.')
        break
    
    else:
        print('Opção invalidade. Tente novamente.')