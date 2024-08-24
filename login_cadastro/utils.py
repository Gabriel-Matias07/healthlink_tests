import sys,time,os, db_utils

#Módulo para funções utilitárias que podem ser usadas em várias partes do programa

#Função que imprime mensagem caso sucesso no cadastro
def msg_sucesso():
    print("\n")
    print("Cadastro realizado com sucesso. ")
    return None

#Função que limpa o terminal e encerra o programa
def encerrar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Programa encerrado. ')
    return None

#Função para animação de inserção de dados
def carregamento():
    time.sleep(1)
    print("Abrindo o Banco de Dados...")
    time.sleep(2)
    print("Inserindo Informações...")
    time.sleep(2)
    return None

#Escreve o texto de apresentação com animação corrida
def escrevendo_texto(texto, atraso):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

#Função que mostra as informações escolhidas pelo usuário
def mostrar_info(informacoes_pessoais, preferencia_user ):
    print("\n")
    print("Informações pessoais:\n")
    for i in informacoes_pessoais:
        print(f"{i}")
    print("\n")
    print("Suas preferências:\n")
    for i in preferencia_user:
        print(f"{i}")
    print("\n")

    return db_utils.salvar_form_usuario(informacoes_pessoais, preferencia_user) #Retorna duas listas como parâmetro