import os


os.system('cls')

# Criando a classe pai
class ClassePai:
    def __init__(self,nome,idade,ano_nascimento): # Metodo construtor
        # Definindo atributos
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = ano_nascimento

# Criando a classe filha
class ClasseFilha(ClassePai): # Classe filha herdando atributos da classe pai
    def __init__(self,nome,idade,ano_nascimento):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = ano_nascimento
    
    # Definindo metodos
    def cadastro(self):
        lista = {}
        
        lista['Nome'] = self.nome
        lista['Idade'] = self.idade
        lista['Ano de Nascimento'] = self.ano_nascimento
        print(lista)

    
nome = str(input('Nome: '))
idade = int(input('Idade: '))
ano_nascimento = int(input('Ano de nascimento: '))
print('-'*70)

exibir = ClasseFilha(nome,idade,ano_nascimento) # Criando um objeto da classe filha

# Usando o objeto Exibir(que é uma objeto da classe filha) para chamar o metodo Cadastro da classe filha
exibir.cadastro()