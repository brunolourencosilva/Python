import os


os.system('cls')

nome = ['Agata', 'Bia', 'Coly', 'Isis']

for indice, nome in enumerate(nome):
    # Cria uma tupla contendo o indice e o nome da pessoa atual.
    minha_tupla = (indice, nome)
    # A variavel minha_tuplas é utilizada para acessar o 
    # indice eo nome armazenados na tupla.
    # Mas posso acessar diretamente os elementos 'indice' e 'nome'
    print(f'O nome "{minha_tupla[1]}", posição {minha_tupla[0]} da lista.')
    print(f'O nome "{nome}", posição {indice} da lista.')
    print('-'*70)