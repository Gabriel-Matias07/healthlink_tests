#Módulo para funções relacionadas ao usuário

import sqlite3
import utils,db_utils,redirect

#Função que permite usuário escolher entre login, cadastro no sistema ou encerrar programa
def usuario(retorno):
    print("Opção 'Usuário' selecionada. \n")
    escolha = input("Selecione 1 para login, 2 para cadastro ou 0 para encerrar: ")
    if escolha == '1':
        print(retorno)
        return login_usuario()
    elif escolha == '2':
        return cadastro_usuario(), redirect.redirecionar(retorno)
    elif escolha == '0':
        return utils.encerrar()
    else:
        print("Resposta Inválida. ")
        return usuario()

#Função mãe de cadastro, ela chama e passa os parâmetros para as outras funções
def cadastro_usuario():
    nome = cadastro_nome()
    email = cadastro_email()
    senha = cadastro_senha()
    confirma_senha(senha)
    utils.carregamento()
    db_utils.inserir_bd_usuario(nome, email, senha)
    utils.msg_sucesso()

def cadastro_nome():
    nome = input("Digite o seu nome: ")
    if not nome:
        print("Nome Inválido")
        return cadastro_nome()
    else:
        return nome

def cadastro_email():
    email = input("Digite o seu email: ")
    if not '@' in email or not '.com' in email:
        print("Um email válido deve conter '@' e '.com'. ")
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
def login_usuario():
    email_login = input("Digite seu email: ")
    senha_login = input("Digite sua senha: ")

    if not '@' in email_login or not '.com' in email_login:
        print("Um email válido deve conter '@' e '.com'")
        return login_usuario()
    else:
        pass
    if len(senha_login) <= 5:
        print("Uma senha válida precisa ter mais de 5 caracteres. ")
        return login_usuario()
    try:
        banco = sqlite3.connect("dados_usuarios.db")
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM dados_usuarios WHERE email = ?", (email_login,)) #Verifica a coluna senha onde email condiz ao parêmetro
        resultado = cursor.fetchone() #Retorna uma tupla contendo o valor da coluna senha

        if resultado:
            senha_salva = resultado[0]
            if senha_login == senha_salva:
                print("Login bem-sucedido.")
            else:
                print("Senha incorreta.")
                resposta = input("Esqueceu sua senha? Digite 1 para recuperar ou 2 para tentar novamente: ")
                if resposta == '1':
                    return recuperar_senha_usuario(email_login)
                elif resposta == '2':
                    return login_usuario()
                else:
                    print("Valor inválido.")
                    return login_usuario()
        else:
            print("Email não encontrado.")
            return login_usuario()
    except sqlite3.Error as error:
        print(error)

#Função que recupera senha do usuário para email especificado        
def recuperar_senha_usuario(email_login):
    email_base = email_login
    nova_senha =  input(f"Digita uma nova senha para o email '{email_login}': ")
    return db_utils.inserir_nova_senha_usuario(nova_senha, email_base)

#Função de formulário do usuário
def form_usuario(dado_retornado):
    print(f"Detectamos que você se cadastrou na nossa plataforma como {dado_retornado}. Iremos precisar de algumas informações para darmos prosseguimento.\n ")
    informacoes_pessoais = []
    endereco = []
    preferencia_user = []

    nome_completo = input("Nome completo: ")
    telefone = input("Telefone: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    numero_casa = input("Número da casa: ")

    #Adicionando valores nas listas
    informacoes_pessoais.append(nome_completo)
    informacoes_pessoais.append(telefone)
    endereco.append(estado)
    endereco.append(cidade)
    endereco.append(bairro)
    endereco.append(numero_casa)

    #Percorre uma lista pré-definida de opções, imprime e recebe da entrada padrão o valor escolhido, inserindo em uma lista
    print("Preferência de contratação.\n ")
    preferencias_contratacao_user = ['Médico', 'Enfermeiro', 'Fisioterapeuta', 'Dentista']

    #Laço pra mostrar a lista de preferências
    i = 1
    for opcao in preferencias_contratacao_user:
            print(f"{i} - {opcao}\n")
            i += 1

    while True:
        resposta = int(input("Digite o número das suas preferências e/ou '0' para encerrar: "))
    
        if resposta == 0:
            mostrar_info(informacoes_pessoais, endereco, preferencia_user)
            break 
    
        if 1 <= resposta <= len(preferencias_contratacao_user):
            preferencia_selecionada = preferencias_contratacao_user[resposta - 1]
            preferencia_user.append(preferencia_selecionada)
            print(f"Você escolheu: {preferencia_selecionada}\n")
        else:
            print("Valor digitado é inválido! Tente novamente.\n")

#Função que mostra as informações escolhidas pelo usuário
def mostrar_info(informacoes_pessoais, endereco, preferencia_user ):
    print("Informações pessoais:\n")
    for i in informacoes_pessoais:
        print(f"{i}\n")
    print("Endereço:\n")
    for i in endereco:
        print(f"{i}\n")
    print("Suas preferências:\n")
    for i in preferencia_user:
        print(f"{i}\n")

    return db_utils.salvar_form_usuario(informacoes_pessoais, endereco, preferencia_user) #Retorna três listas como parâmetro