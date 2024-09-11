import csv
import os



class ContaBancaria:
    def __init__(self,numero_conta,nome_titular,saldo,agencia,tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        
# Função para obter dados do usuario e criar uma substancia de ContaBancaria
def obter_dado_conta():
    numero_conta = input('Digite o numero da conta: ')
    nome_titular = input('Digite o nome do titular: ')
    saldo = float(input('Digite o saldo inicial: '))
    agencia = input('Digite a agencia: ')
    tipo_conta = input('Digite o tipo de conta: ')
    return ContaBancaria(numero_conta,nome_titular,saldo,agencia,tipo_conta)

# Lista para armazenar contas bancarias
contas = []

# Obter dados das contas
while True:
    conta = obter_dado_conta()
    contas.append({
        'numero_conta': conta.numero_conta,
        'nome_titular': conta.nome_titular,
        'saldo': conta.saldo,
        'agencia': conta.agencia,
        'tipo_conta': conta.tipo_conta
    })
    continuar = input('Deseja adicionar outra conta? (s/n): ')
    if continuar.lower() != 's':
        break
    
# Caminho para a pasta onde o arquivo CSV sera salvo
pasta = 'arquivo_csv/conta/'

# Verificando se a pasta existe, se não,ira cria-la
os.makedirs(pasta,exist_ok=True)

# Nome o para o arquivo CSV para gravar as informaçoes
arquivo = 'arquivos_csv/conta/conta.csv'

# Escrever a lista de dicionario no arquivo csv
with open(arquivo,mode='w', newline='') as conta:
    fieldnames = ['numero_conta','nome_titular',
                  'saldo','agencia','tipo_conta']
    writer = csv.DictWriter(conta,fieldnames=fieldnames,delimiter=';')
    
    writer.writeheader()
    for registro in contas:
        writer.writerow(registro)

print(f'As informações das contas foram salvas em {arquivo}')