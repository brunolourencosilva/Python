import csv
import os


os.system('cls')

arquivo = 'aulas/aula018_arquivos/alunas.csv'
nome_para_apagar = input('Digite o nome que deseja apagar: ')

# Lenda os dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)
    
# Verificando se o nome existe e apagando o registro
apagado = False
novo_cadastro = [registro for registro in cadastro \
                if registro['Nome'] != nome_para_apagar]

if len(novo_cadastro) < len(cadastro):
    apagado = True
    
# Reescrevendo o arquivo com os dados atualizados
with open(arquivo, 'w' , newline='') as arquivos_csv:
    campos = ['Nome' , 'Telefone' , 'Cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(novo_cadastro)
print('-'*70)
if apagado:
    print(f'Registro com nome {nome_para_apagar} apagado com sucesso.')
else:
    print(f'Registro com nome {nome_para_apagar} não encontrado.')
print('-'*70)