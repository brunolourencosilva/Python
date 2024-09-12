import os
from datetime import datetime


class Usuario:
    def __init__(self, nome, data_nascimento):
        # Chama o setter para definir o nome
        self.set_nome(nome)
        # Chama o setter para definir a data de nascimento
        self.set_data_nascimento(data_nascimento)
        
    def get_nome(self):
        # Retorna o nome do usuario
        return self._nome
    
    def set_nome(self, nome):
        # Define uma nova variavel para nome (_nome)
        self._nome = nome
    
    def get_data_nascimento(self):
        # Retorna a data d nascimento do usuario
        return self._data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        # Define uma nova variavel para a data de nascimento
        self._data_nascimento = data_nascimento
        
        # Calcula a idade do usuario
        # Obtem a data e hora atuais
        hoje = datetime.now()
        
        # Converte a data de nascimento de string para um objeto datime
        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        # Calcula a idade subtraindo o ano de nascimento do ano atual e
        # ajusta se a data de aniversario ainda não ocorreu neste ano
        self._idade = hoje.year - nascimento.year - \
            ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    
    def get_idade(self):
        # Retorna a idade do usuario
        return self._idade

os.system('cls')
print('-'*70)
print('Programar para encontrar idade')
print('='*70)
nome = input('Digite seu nome: ')
data_nascimento = input('Data de nascimento (dd/mm/yyyy): ')

# Cria uma instancia da classe Usuario
usuario = Usuario(nome,data_nascimento)

# Exibe o nome, data de nascimento e idade do usuario
print('-'*70)
print(f'Nome: {usuario.get_nome()}')
print(f'Data de Nascimento: {usuario.get_data_nascimento()}')
print(f'Idade: {usuario.get_idade()} anos')
print('-'*70)