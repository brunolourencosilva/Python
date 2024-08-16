import csv
import os


os.system('cls')

arquivo = 'aulas/aula018_arquivos/alunas.csv'

nome_para_alterar = input('Nome que deseja procurar: ')


# Ler os dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    cadastro = list(leitura)

# Verificando se o nome existe e alterando o registro
alterado = False

for registro in cadastro:
    if registro['Nome'] == nome_para_alterar:
        print(f"Registro encontrado: {registro}")
        novo_nome =  input(f'Novo nome: ')
        novo_telefone =  input(f'Novo telefone: ')
        nova_cidade = input(f'Nova cidade: ')
        
        if novo_nome:
            registro['Nome'] = novo_nome
        if novo_telefone:
            registro['Telefone'] = novo_telefone
        if nova_cidade:
            registro['Cidade'] = nova_cidade
        alterado = True

# Reescrevendo o arquivo com os dados atualizados
# if alterado:
with open(arquivo, 'w', newline='') as arquivo_csv:
    campos = ['Nome', 'Telefone', 'Cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
        
    escrever.writeheader()
    escrever.writerows(cadastro)
print('-'*70)

if alterado:
    print(f'Registro com nome {nome_para_alterar} alterado com sucesso.')
else:
    print('-'*70)
    print(f'Registro com nome {nome_para_alterar} não encontrado.')
print('-'*70)