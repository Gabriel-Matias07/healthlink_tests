import sys,time
import user,professional,redirect,utils

#Módulo que vai chamar as funções principais de outros módulos

#Função que apresenta um resumo do programa
def apresentacao():
    print("\n")
    print("----Bem Vindo ao HealthLink----\n")

    #Escreve o texto de apresentação com animação corrida
    def escrevendo_texto(texto, atraso):
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(atraso)
        print()

    texto = "----O HealthLink é uma plataforma inovadora voltada para a área da saúde, desenvolvida para facilitar a comunicação direta e a contratação de profissionais de saúde.\n Nossa missão é democratizar o acesso aos serviços de saúde, conectando pacientes e profissionais de maneira eficiente e segura.----\n"
    escrevendo_texto(texto, atraso=0.005)

#Função para escolher entre prestador de serviços (profissiona), cliente (usuário) ou encerrar programa
def escolher_opcao():
    escolha = input("Digite 1 para Usuário, 2 para Profissional ou 0 para encerrar: ")
    if escolha == '1':
        retorno = "usuário"
        return user.usuario(retorno)
    elif escolha == '2':
        retorno = "profissional"
        return professional.profissional(retorno)
    elif escolha == '0':
        return utils.encerrar()
    else:
        print("Resposta inválida. ")
        return escolher_opcao()

apresentacao()
escolher_opcao()