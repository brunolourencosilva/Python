import os

# Podemos importa so as funções que queremos utilizar
from datetime import datetime
from datetime import date



os.system('cls')

# Declarando uma variavel para data
data = datetime.now()

# Declarando uma variavel para data formatada
data_formada = data.strftime('%d/%m/%Y')

# Declarando uma variavel para data e hora formatada
data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada: {data_formada}')
print(f'Data e hora formatada: {data_hora_formatada}')

# Recebendo ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# Imprimindo a data atual e o nascimento
print('-'*70)
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento...........: {nascimento}')

#imprimindo so o ano
print(f'ano atual............: {data_atual.year}')

#imprimindo só a idade
print(f'Sua idade é:.........: {idade} anos')
print('-'*70)