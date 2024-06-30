# curso de desenvolvimento de sistema
# autor:Bruno Lourenço
# data:1/07/2024
# atividade009 G-Faça um programa para cadastrar os alunos de uma escola.
# Para os campos, tome como referência o nome do aluno, data de nascimento e matrícula.


import os


os.system('cls')

print('='*70)
print('Programa que cadastra alunos de uma escola.')
print('-'*70)

# Declaração de dicionario
dicionario = { }
lista = []
while True:
    os.system('cls')
    print('Escola de magia pyromaniaca Incendialis.')
    print()
    print('Opções')
    print('1.Cadastrar aluno')
    print('2.Mostrar os alunos cadastrados')
    print('3.Sair')
    
    opcao = int(input('Escolha uma opção: '))
    print('-'*70)
    
    if opcao == 1: # Adicionar um novo aluno
        os.system('cls')
        print('-'*70)
        print(f'Informe os dados do aluno')
        nome = (input('Nome do aluno: '))
        data_nascimento = (input('Data de nascimento: '))
        matricula = (input('Data da matrícula: '))

        print('.'*70)
        
        # Adicionando os dados ao dicionario
        dicionario['Nome do aluno'] = nome
        dicionario['Data de nascimento'] = data_nascimento
        dicionario['Data da matrícula'] = matricula
        
        lista.append(dicionario.copy())# Adicionando uma copia a lista
        
        print('Aluno cadastrado!!')
        print(f'Informações do aluno:')
        print(dicionario)
        input('\nPressione Enter para continuar...')
        os.system('cls')
        
    elif opcao == 2: #  Mostra os alunos adicionados
        if dicionario:
            os.system('cls')
            print('-'*70)
            print('Alunos cadastrados:')
            print('-'*70)
            for aluno in lista:  # Itera sobre cada dicionário de alunos na lista 'lista'
                for chave, valor in aluno.items():
                    print(f'{chave}: {valor}') # Imprime a chave e o valor formatados
                print('-'*70)
            input('\nPressione Enter para continuar...')
        else:
            print('Sem alunos cadastrados!!')
            input('\nPressione Enter para continuar...')
            os.system('cls')
    
    elif opcao == 3: # Encerra o programa
        os.system('cls')
        print('-'*70)
        print('Fim do programa')
        print('Obrigado por escolher a escola Incendialis.')
        print('Tenha um bom dia e que a Fenix ilumine seu caminho.')
        print('-'*70)
        break
    
    else:
        print('-'*70)
        print('Opção invalida!!!')
        print()
        input('\nPressione Enter para continuar...')
