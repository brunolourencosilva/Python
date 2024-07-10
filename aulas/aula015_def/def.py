def limpa_tela():
    """Função limpar o terminal
    """    
    import os
    os.system('cls')
    

def soma(a,b):
    """Função para soma 2 numeros

    Args:
        a (int): Valor de A
        b (int): Valor de B

    Returns:
        Retorna a soma de 2 numeros
    """    
    return a + b


def firula():
    print('-'*70)

# Programa principal


# Chamando a função
limpa_tela()
firula()
resposta = soma(1,2)
print(f'A soma do numeros é: {resposta}')
firula()
print()