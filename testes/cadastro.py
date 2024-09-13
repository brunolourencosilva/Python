import os


os.system('cls')


class ClassePai:
    def __init__(self,nome,idade,ano_nascimento):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = ano_nascimento

class ClasseFilha(ClassePai):
    def __init__(self,nome,idade,ano_nascimento):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = ano_nascimento
    
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
exibir = ClasseFilha(nome,idade,ano_nascimento)
exibir.cadastro()