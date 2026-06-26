# Modulo criado por Filipe Cavinato

def gerar_senha(tamanho):
    from random import choice
    caracteres = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '1234567890'
    caracter_especial = '@#$&*!?-_'
    senha = ''
    while len(senha) < tamanho:
        if choice([True, False]):
            senha += choice(caracteres).upper()
            if len(senha) < tamanho:
               senha += choice(numeros)
        else:
            senha += choice(caracteres)
            if len(senha) < tamanho:
                senha += choice(caracter_especial)
    return senha
