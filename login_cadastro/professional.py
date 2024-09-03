#Módulo para funções relacionadas ao profissional

import pwinput
import utils,db_utils,redirect

#Função que permite profissional escolher entre login, cadastro no sistema ou encerrar programa
def profissional(retorno):
    print("Opção 'Profissional' selecionada. \n")
    escolha = input("Selecione 1 para login, 2 para cadastro ou 0 para encerrar: ")
    if escolha == '1':
        print(retorno)
        return db_utils.login_profissional()
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

#Função que recupera senha do usuário para email especificado        
def recuperar_senha_profissional(email_login):
    email_base = email_login
    nova_senha =  input(f"Digita uma nova senha para o email '{email_login}': ")
    profissional.inserir_nova_senha_profissional(nova_senha, email_base)

def form_profissional(dado_retornado):
    print(f"Detectamos que você se cadastrou na nossa plataforma como {dado_retornado}. Iremos precisar de algumas informações para darmos prosseguimento.\n ")
    informacoes_pessoais = []
    preferencia_prof = [] 
    
    telefone = input("Telefone: ")
    estado = input("Estado: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    numero_casa = input("Número da casa: ")

    informacoes_pessoais.append(telefone)
    informacoes_pessoais.append(estado)
    informacoes_pessoais.append(cidade)
    informacoes_pessoais.append(bairro)
    informacoes_pessoais.append(numero_casa)

   
    #Percorre uma lista pré-definida de opções, imprime e recebe da entrada padrão o valor escolhido, inserindo em uma lista
    print("Preferência de contratação.\n ")
    preferencias_contratacao_prof = ['Médico', 'Enfermeiro', 'Fisioterapeuta', 'Dentista']

    #Laço pra mostrar a lista de preferências
    i = 1
    for opcao in preferencias_contratacao_prof:
            print(f"{i} - {opcao}\n")
            i += 1

    while True:
        resposta = int(input("Digite o número das suas preferências e/ou '0' para encerrar: "))
    
        if resposta == 0:
            utils.carregamento()
            db_utils.salvar_form_profissional(telefone, estado, cidade, bairro, numero_casa)
            break
        if 1 <= resposta <= len(preferencias_contratacao_prof):
            preferencia_selecionada = preferencias_contratacao_prof[resposta - 1]
            preferencia_prof.append(preferencia_selecionada)
            print(f"Você escolheu: {preferencia_selecionada}\n")
        else:
            print("Valor digitado é inválido! Tente novamente.\n")