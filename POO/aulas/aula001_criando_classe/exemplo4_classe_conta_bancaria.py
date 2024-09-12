import os


class Banco():
    def __init__(self,nome='',agencia=0,conta=0,cpf=0,conta_corrente=0,poupanca=0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.poupanca = poupanca
        
    def deposito(self,valor):
        escolha = input ('Conta Corrente (cc) ou poupanca (po)? ').lower().strip
        
        if escolha == 'cc':
            print(f'Valor do deposito: (+)R${valor}')
            print(f'Saldo anterior (CC): R${self.conta_corrente}')
            self.conta_corrente += valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('-'*70)
        
        elif escolha == 'po':
            print(f'\nValor do deposito: (+)R${valor}')
            print(f'\nSaldo anterior na poupança R${self.poupanca}')
            self.poupanca += valor
            print(f'\tSaldo atual na poupaça: R${self.poupanca}')
            print('-'*70)
            
        else:
            print('Opção invalida!!!')
            
    def saque(self,valor):
        escolha = input('Conta corrente (cc) ou Poupança (po)? ').lower().strip()
        
        if escolha == 'cc':
            print(f'\nValor sacado: (-)R${valor}')
            print(f'\nSaldo anterior na CC: R${self.conta_corrente}')
            self.conta_corrente -= valor
            print(f'\tSaldo atual na cc: R${self.conta_corrente}')
            print('-'*70)
        
        elif escolha == 'po':
            print(f'\nValor sacado: (-)R${valor}')
            print(f'\nSaldo anterior em poupança: R${self.poupanca}')
            self.poupanca -= valor
            print(f'\tSaldo atual na poupanca: R${self.poupanca}')
            print('-'*70)
            
        else:
            print('Opção invalida!!!')
            
os.system('cls')

# Coletar dados do usuario para  criar uma nova conta
print('Digite os dados para criar uma nova conta: ')
nome = input('Nome: ')
agencia = int(input('Agencia: '))
conta = int(input('Numero da conta: '))
cpf = int(input('CPF: '))
conta_corrente = float(input('Saldo inicial da conta conrrente: '))
poupanca = float(input('Saldo inicial da poupanca: '))

# Criar um novo correntista
correntista = Banco(nome,agencia,conta,cpf,conta_corrente,poupanca)

print('-'*70)
print('Movimentação Bancaria')
print('='*70)
opcao = input('Deposito ou saque (D/S)? ').upper().strip

if opcao == 'D':
    valor = float(input('Qual o valor do deposito? '))
    correntista.deposito(valor)

elif opcao == 'S':
    valor = float(input('Qual o valor do saque? '))
    correntista.saque(valor)

else:
    print('Opção invalida')