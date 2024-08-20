import os


class Pessoa:
    def __init__(self, nome,cpf,nascimento,cep,cidade,estado):
        # Inicinado os atributos
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

# Solicitando entrada de dados do usuario
os.system('cls')
print('-'*70)
nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
nascimento = ('Digite o ano de nascimento: ')
cep = input('Digite o CEP: ')
cidade = input('Digite a cidade: ')
estado = input('Digite o estado: ')

# Criando um objeto da classe Pessoa com os dados fornecidos pelo usuario
Pessoa1 = Pessoa(nome, cpf,nascimento,cep,cidade,estado)

# Acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInformação da Pessoa: ')
print('='*70)
print(f'Nome: {Pessoa1.nome}')
print(f'CPF: {Pessoa1.cpf}')
print(f'Ano de nascimento: {Pessoa1.nascimento}')
print(f'CEP: {Pessoa1.cep}')
print(f'Cidade: {Pessoa1.cidade}')
print(f'Estado: {Pessoa1.estado}')
print('-'*70)