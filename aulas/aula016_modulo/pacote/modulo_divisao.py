def dividir(a,b):
    """Metodos para dividir 2 numeros

    Args:
        a (any): Dividendo
        b (any): Divisor

    Returns:
        str: Mensagem de erro ou 'ok!' se a dvisão for bem sucedida
        any: Quociente ou None em caso de erro
    """    
    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a / b
    return divisao, 'ok'