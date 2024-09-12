import os
from abc import ABC,abstractmethod

# Classe abstrata
class MetodoDePagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self,valor):
        # Processo um pagamento qualquer
        pass

# Subclasse concreta
class CartãoDeCredito(MetodoDePagamento):
    
    def processar_pagamento(self, valor):
        print(f'Pagamento com cartão de credito.')
        print(f'Valor Pago: R${valor}')

# Subclasse concreta
class Boleto(MetodoDePagamento):
    
    def processar_pagamento(self, valor):
        print(f'Emissão de Boleto')
        print(f'Pagamento de R${valor}.')


os.system('cls')
# Instanciando as classes filhas
pagamento_cartao = CartãoDeCredito()
pagamento_cartao.processar_pagamento(5000.00)

pagamento_boleto = Boleto()
pagamento_boleto.processar_pagamento(500.00)