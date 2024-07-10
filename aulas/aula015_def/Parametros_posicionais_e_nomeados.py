import os


os.system('cls')

# Definindo a função
def dados_paciente(nome='Coly',nascimento=2005,peso=46,altura=1.68):
    print(f'Bem vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}.')
    print(f'o peso da {nome} é {peso}Kg.')
    print(f'A altura da {nome} é {altura}.')
    print('-'*70)
    
# Iniciando para lembrar
def posicional_nomeado(nascimento, nome='Coly', ):
    print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
    print(f'O ano de nascimento da {nome} é {nascimento}!')
    print(f'-'*70)


# def nomeado_posicional(nome='Coly', nascimento):
#     print(f'Bem-vindo(a) ao sistema Senac, {nome}!')
#     print(f'O ano de nascimento da {nome} é {nascimento}.')
#     print(f'-'*70)
# Fim para lembra


# Invocando a função
dados_paciente()

dados_paciente(nome='Isis',nascimento=1985,peso=46,altura=1.56)
dados_paciente(nascimento=2008,nome='Agata',peso=46,altura=1.58)
dados_paciente(altura=1.56,peso=46,nome='Bia',nascimento=1985,)