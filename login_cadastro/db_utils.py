
import time,sqlite3, os
import user,professional

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
        #os.system('cls' if os.name == 'nt' else 'clear')
        return user.login_usuario()
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
        return professional.login_profissional()
    except sqlite3.Error as error:
        print(error)

#Função que adiciona informações do formulário do usuário ao banco de dados
def salvar_form_usuario(informacoes_pessoais, endereco, preferencia_user):
    #A ideia é percorrer as listas e adicionar cada item ao uma tabela do banco de dados
    return None