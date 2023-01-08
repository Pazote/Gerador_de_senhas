from random import choice
import string

banco_senha = []

def gerar_senha(tamanho_senha):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for i in range(tamanho_senha):
        senha += choice(caracteres)
    print("Senha gerada: {}".format(senha))
    _armazenar_senha(senha)


def _coletar_resposta():
    resposta = str(input("Você gostaria de gerar uma nova senha?{y/n} \n"))
    return resposta



def _coletar_tamanho():
    tamanho = int(input("Qual o número de caracteres da senha? \n"))
    return tamanho


def _armazenar_senha(senha):
    banco_senha.append(senha)


def _historico():
    print(banco_senha)


def consultar_historico():
    quero_consultar = str(input("Você gostaria de consultar uma lista das senhas geradas?{y/n} \n"))
    if quero_consultar == 'y':
        _historico()
    else:
        pass




def init():
    m = _coletar_resposta()
    if m == 'y':
        n = _coletar_tamanho()
        gerar_senha(n)
        init()
    if m == 'n':    
        consultar_historico()
    if m != 'y' and m != 'n':
        print("resposta inválida")
        init()



#main

init()