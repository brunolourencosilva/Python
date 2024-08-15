import csv
import os


lista = [
    {'Nome':'Agata','Telefone': '(32)99196-0000', 'Cidade': 'Juiz de fora'},
    {'Nome':'Bia','Telefone': '(32)99196-1111', 'Cidade': 'Juiz de fora'},
    {'Nome':'Coly','Telefone': '(32)99196-2222', 'Cidade': 'Juiz de fora'},
    {'Nome':'Isis','Telefone': '(32)99196-3333', 'Cidade': 'Juiz de fora'},
]

# Caminho para a pasta onde  o arquivo csv sera salvo
pasta = 'aulas/aula018_arquivos'

# Verificando se a pasta existe, se não,ira cria-la
os.makedirs(pasta, exist_ok=True)

# Nome para o arquivo csv para gravar as informações
arquivo = 'aulas/aula018_arquivos/alunas.csv'

# Caminho completo do arquivo csv
caminho_arquivo = os.path.join(pasta, arquivo)

# Abre o arquivo 'arquivo' no modo de escrita ('w').
# Se o arquivo não existir,ele sera criado; se exixstir, sera truncado (esvaziado).
# Newline='' : Evita a adição de linhas em brancos extras ao gravar o arquivo em algumas plataforma.
# As arquivos_csv: Atribui o objeto arquivos ao 'arquivos_csv' para ser usado dentro do bloco with.
with open(arquivo, 'w', newline='') as arquivo_csv:
    
    # Campos = ["name", "telefone", "cidade"]: Define a lista de nomes de campos
    # (cabeçalhos das colunas do csv).
    campos = ['Nome', 'Telefone', 'Cidade']
    
    # writer = csv.DictWriter(arquivos_csv, fieldnames=campos):
    # Cria um obejeto dictWriter que usara 'arquivos_csv' para gravar os campos.
    # fieldnames define a ordem dos campos no arquivos CSV.
    # delimiter=';': é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    # Writer.writerheader(): Grava a linha de cabeçalhos no
    # arquivos csv usando os nomes de campos definidos em fieldnames
    escrever.writeheader()
    
    # writer.writerows(): Grava todas as linhas da lista no arquivos csv.
    # Cada dicionario em 'Lista' se torna uma linha no arquivo.
    escrever.writerows(lista)

os.system('cls')
# Exibe um mensagem indicando que o arquivo foi gravado com sucesso
print(f'Arquivos {arquivo} gravado com sucesso')