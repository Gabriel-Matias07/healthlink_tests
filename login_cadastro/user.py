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
    preferencias_contratacao_user = ['Médico', 'Enfermeiro', 'Fisioterapeuta']

    #Laço pra mostrar a lista de preferências
    for opcao in preferencia_user:
        for i in range(len(preferencia_user) + 1):
            print(f"{opcao}\n")
    con = True
    while con:
        resposta = int(input("Digite o número das suas preferências e/ou '0' para encerrar: "))
        if resposta == 0:
            con = False
        else:
            for i in preferencia_user:
                if resposta == preferencia_user[i]:
                    preferencias_contratacao_user.append(resposta)
            else:
                print("Valor digitado é inválido! ")
                con = True

#Função que mostra as informações escolhidas pelo usuário
def mostrar_info(reposta, preferencia_user):



    for i in range(len(preferencias_contratacao_user)):
        print(f"{i + 1} - {preferencias_contratacao_user[i]}" )
    print("\n")
    resposta = int(input("Selecione sua prefência: "))
    for i in range(len(preferencias_contratacao_user)):
        resposta = int(resposta - 1)
        if resposta == i:
            add = preferencias_contratacao_user[i]
            print(add)
            preferencia_user.append(add)
    print(preferencia_user)

    return salvar_form_usuario(informacoes_pessoais, endereco, preferencia_user)


#Função que armazena as informações permanentemente
def salvar_form_usuario(informacoes_pessoais, endereco, preferencia_user):
    arquivo = open("dados_form.txt", "a")
    for i in informacoes_pessoais:
        arquivo.write(f"{i}")
    for i in endereco:
        arquivo.write(f"{i}")
    arquivo.close()
    for i in preferencia_user:
        arquivo.write(f"{i}")
    return None