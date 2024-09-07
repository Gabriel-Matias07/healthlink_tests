
import time,sqlite3, os
import user,professional, utils
import pwinput

#Módulo específico para interações com o banco de dados

#Função que insere os dados do cliente no banco de dados
def inserir_bd_usuario(nome, email, senha):
    erro = False
    try:
        banco = sqlite3.connect("dados_usuarios.db") #Conecta o banco de dados
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados_usuarios (nome text, email text, senha text)") #Cria o banco caso não exista
        cursor.execute("SELECT COUNT(*) AS existe_login FROM dados_usuarios WHERE email = ?", (email, )) #Verifica se o email já existe no banco
        existe_login = cursor.fetchone()[0]

        if existe_login > 0:
            print("Email já cadastrado. Insira um endereço de email não cadastrado. ")
            erro = True
        else:
            cursor.execute(f"INSERT INTO dados_usuarios VALUES (?, ?, ?)", (nome, email, senha)) #Insere os valores no banco
            banco.commit()
            banco.close()

    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro

#Função que insere os dados do profissional no banco de dados
def inserir_bd_profissional(nome, email, senha):
    erro = False
    try:
        banco = sqlite3.connect("dados_profissionais.db") #Conecta o banco de dados
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados_profissionais (nome text, email text, senha text)") #Cria o banco caso não exista
        cursor.execute("SELECT COUNT(*) AS existe_login FROM dados_profissionais WHERE email = ?", (email, )) #Verifica se o email já existe no banco
        existe_login = cursor.fetchone()[0]

        if existe_login > 0:
            print("Email já cadastrado. Insira um endereço de email não cadastrado. ")
            erro = True
        else:
            cursor.execute(f"INSERT INTO dados_profissionais VALUES (?, ?, ?)", (nome, email, senha)) #Insere os valores no banco
            banco.commit()
            banco.close()

    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro

#Função que insere a nova senha no banco de dados
def inserir_nova_senha_usuario(nova_senha, email_base):
    try:
        banco = sqlite3.connect("dados_usuarios.db")
        cursor = banco.cursor()
        cursor.execute("UPDATE dados_usuarios SET senha = ? WHERE email = ?", (nova_senha, email_base)) #Atualiza a senha para o email de parâmetro
        banco.commit()
        banco.close()
        time.sleep(2)
        print("Atualizando senha...")
        time.sleep(2)
        print("Senha atualizada com sucesso.")
        time.sleep(0.5)
        print("Retornando para o login...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return login_usuario()
    except sqlite3.Error as error:
        print(error)

#Função que insere a nova senha no banco de dados
def inserir_nova_senha_profissional(nova_senha, email_base):
    try:
        banco = sqlite3.connect("dados_profissionais.db")
        cursor = banco.cursor()
        cursor.execute("UPDATE dados_profissionais SET senha = ? WHERE email = ?", (nova_senha, email_base)) #Atualiza a senha para o email de parâmetro
        banco.commit()
        banco.close()
        time.sleep(2)
        print("Atualizando senha...")
        time.sleep(2)
        print("Senha atualizada com sucesso. ")
        time.sleep(0.5)
        print("Retornando para o login...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return login_profissional()
    except sqlite3.Error as error:
        print(error)

#Função para verificar se o login existe e logar no sistema
def login_usuario():
    email_login = input("Digite seu email: ")
    """ senha_login = input("Digite sua senha: ") """
    senha_login = pwinput.pwinput(prompt = 'Digite sua senha: ')

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
                    return user.recuperar_senha_usuario(email_login)
                elif resposta == '2':
                    return login_usuario()
                else:
                    print("Valor inválido.")
                    return login_usuario()
        else:
            print("Email não encontrado.")
            return login_usuario()
    except sqlite3.Error as error:
        print(f"Erro retornado: {error}")
        print("Talvez você não tenha feito seu cadastro.")

#Função para verificar se o login existe e logar no sistema
def login_profissional():
    email_login = input("Digite seu email: ")
    """ senha_login = input("Digite sua senha: ") """
    senha_login = pwinput.pwinput(prompt = 'Digite sua senha: ')

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
                    return professional.recuperar_senha_profissional(email_login)
                elif resposta == '2':
                    return login_profissional()
                else:
                    print("Valor inválido.")
                    return login_profissional()
        else:
            print("Email não encontrado.")
            return login_profissional()
    except sqlite3.Error as error:
        print(f"Erro retornado: {error}")
        print("Talvez você não tenha feito seu cadastro.")

#Função que adiciona informações do formulário do usuário ao banco de dados
def salvar_form_usuario(telefone, estado, cidade, bairro, numeroCasa):
    erro = False
    try:
        banco = sqlite3.connect("informacoes_user.db")
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS informacoes_user (telefone text, estado text, cidade text, bairro text, numeroCasa text)") #Cria o banco caso não exista
        cursor.execute(f"INSERT INTO informacoes_user VALUES (?, ?, ?, ?, ?)", (telefone, estado, cidade, bairro, numeroCasa)) #Insere os valores no banco
        banco.commit()
        banco.close()
        utils.msg_sucesso()
    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro

#Função que adiciona informações do formulário do profissional ao banco de dados
def salvar_form_profissional(telefone, estado, cidade, bairro, numeroCasa):
    erro = False
    try:
        banco = sqlite3.connect("informacoes_prof.db")
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS informacoes_prof (telefone text, estado text, cidade text, bairro text, numeroCasa text)") #Cria o banco caso não exista
        cursor.execute(f"INSERT INTO informacoes_prof VALUES (?, ?, ?, ?, ?)", (telefone, estado, cidade, bairro, numeroCasa)) #Insere os valores no banco
        banco.commit()
        banco.close()
        utils.msg_sucesso()
    except sqlite3.Error as error:
        print(error)
        erro = True
    return erro