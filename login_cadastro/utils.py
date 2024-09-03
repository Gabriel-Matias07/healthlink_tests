import sys,time,os, db_utils

#Módulo para funções utilitárias que podem ser usadas em várias partes do programa

#Função que imprime mensagem caso sucesso no cadastro
def msg_sucesso():
    print("\n")
    print("Cadastro realizado com sucesso. ")
    return None

#Função que limpa o terminal ao ser chamada
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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