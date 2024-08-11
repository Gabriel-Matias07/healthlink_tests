#Módulo para funções relacionadas ao profissionak

import sqlite3
import utils,db_utils,redirect

#Função que permite profissional escolher entre login, cadastro no sistema ou encerrar programa
def profissional(retorno):
    print("Opção 'Profissional' selecionada. \n")
    escolha = input("Selecione 1 para login, 2 para cadastro ou 0 para encerrar: ")
    if escolha == '1':
        print(retorno)
        login_profissional()
    elif escolha == '2':
        cadastro_profissional(), redirect.redirecionar(retorno)
    elif escolha == '0':
        utils.encerrar()
    else:
        print("Resposta inválida. ")
        return profissional()
    
#Função mãe de cadastro, ela chama e passa os parâmetros para as outras funções (profissional)
def cadastro_profissional():
    nome = cadastro_nome()
    email = cadastro_email()
    senha = cadastro_senha()
    confirma_senha(senha)
    utils.carregamento()
    db_utils.inserir_bd_profissional(nome, email, senha)
    utils.msg_sucesso()

def cadastro_nome():
    nome = input("Digite o seu nome: ")
    if not nome:
        print("Nome inválido. ")
        return cadastro_nome()
    else:
        return nome

def cadastro_email():
    email = input("Digite o seu email: ")
    if not '@' in email or not '.com' in email:
        print("Um email válido deve conter '@' e '.com'")
        return cadastro_email()
    else:
        return email

def cadastro_senha():
    senha = input("Digite a sua senha: ")
    if len(senha) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return cadastro_senha()
    else:
        return senha

def confirma_senha(senha):
    conf_senha = input("Confirme sua senha: ")
    if senha != conf_senha:
        print("As senhas são diferentes. ")
        return confirma_senha(senha)
    else:
        return None
    
#Função para verificar se o login existe e logar no sistema
def login_profissional():
    email_login = input("Digite seu email: ")
    senha_login = input("Digite sua senha: ")

    if not '@' in email_login or not '.com' in email_login:
        print("Um email válido deve conter '@' e '.com'")
        return login_profissional()
    else:
        pass
    if len(senha_login) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return login_profissional()
    try:
        banco = sqlite3.connect("dados_profissionais.db")
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM dados_profissionais WHERE email = ?", (email_login,)) #Verifica a coluna senha onde email condiz ao parêmetro
        resultado = cursor.fetchone() #Retorna uma tupla contendo o valor da coluna senha

        if resultado:
            senha_salva = resultado[0]
            if senha_login == senha_salva:
                print("Login bem-sucedido. ")
            else:
                print("Senha incorreta. ")
                resposta = input("Esqueceu sua senha? Digite 1 para recuperar ou 2 para tentar novamente: ")
                if resposta == '1':
                    return recuperar_senha_profissional(email_login)
                elif resposta == '2':
                    return login_profissional()
                else:
                    print("Valor inválido.")
                    return login_profissional()
        else:
            print("Email não encontrado.")
            return login_profissional()
    except sqlite3.Error as error:
        print(error)

#Função que recupera senha do usuário para email especificado        
def recuperar_senha_profissional(email_login):
    email_base = email_login
    nova_senha =  input(f"Digita uma nova senha para o email '{email_login}': ")
    profissional.inserir_nova_senha_profissional(nova_senha, email_base)

def form_profissional():
    print("Em breve")