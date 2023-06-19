from getpass import getpass
from funcoes_projeto import add_aluno,add_professor,converter_file_dict, analise_login_senha
import subprocess
    

# Aqui abrimos o arquivo apenas para leitura
file_adm = open("doc_dados\\administradores.txt","r")
file_alunos = open("doc_dados\\alunos.txt","r")

dicionario_adms = {}
dicionario_alunos={}
dicionario_escolhido= {}

converter_file_dict(file_adm,dicionario_adms)
converter_file_dict(file_alunos, dicionario_alunos)

lista_emails_professores = dicionario_adms.keys()
lista_emails_alunos = dicionario_alunos.keys()

print(dicionario_adms)

# Calculamos a quantidade de linhas do arquivo para podermos utilizar esse dado no if logo abaixo
tamanho_linhas_alunos = len(file_alunos.readlines())
# O .seek(0) serve basicamente para resetarmos readline e readlines do arquivo
file_alunos.seek(0)

print(dicionario_alunos)
tentando_entrar_1 = False
tentando_entrar_2 = False

while tentando_entrar_1 == False:
    try:
        entrar = int(input("Digite 1 - Para Logar | 2 - Para se cadastrar: "))
        if entrar == 1:
            tentando_entrar_1 = True
            
            while tentando_entrar_2 == False:
                escolha = input("Digite 1 - logar como professor | 2 - logar como aluno: ")
                #Logando como professor / administrador
                if escolha == "1":
                    tentando_entrar_2 = True

                    login = input("Digite seu email: ").strip()
                    senha = getpass("Digite sua senha: ",stream=None)
                    if analise_login_senha(login, senha, dicionario_adms)==True:
                        print("Login efeuado com sucesso!")
                        subprocess.run(["python","adm_tela.py"])
                    else:
                        if analise_login_senha(login, senha, dicionario_adms) == "Senha incorreta":
                            print("Senha incorreta! Tente denovo.")
                            while True:
                                senha = getpass("Digite sua senha: ",stream=None)
                                if analise_login_senha(login, senha, dicionario_adms)==True:
                                    print("Login efetuado com sucesso!")
                                    break
                                print("Senha incorreta! Tente denovo.")
                            subprocess.run(["python","adm_tela.py"])
                        else:
                            print(analise_login_senha(login, senha, dicionario_adms))
                #Logando como aluno
                elif escolha == "2":
                    tentando_entrar_2 = True

                    login = input("Digite seu email: ").strip()
                    senha = getpass("Digite sua senha: ",stream=None)
                    if analise_login_senha(login, senha, dicionario_alunos)==True:
                        print("Login efeuado com sucesso!")
                        subprocess.run(["python","aluno_tela.py"])
                    else:
                        if analise_login_senha(login, senha, dicionario_alunos) == "Senha incorreta":
                            print("Senha incorreta! Tente denovo.")
                            while True:
                                senha = getpass("Digite sua senha: ",stream=None)
                                if analise_login_senha(login, senha, dicionario_alunos)==True:
                                    print("Login efetuado com sucesso!")
                                    break
                                print("Senha incorreta! Tente denovo.")
                            # subprocess.run(["python","aluno_tela.py"])
                        else:
                            print(analise_login_senha(login, senha, dicionario_alunos))
                else:
                    print("Tipo de acesso inválido! Tente denovo.")
        elif entrar == 2:
            tentando_entrar_1=True

            while tentando_entrar_2 == False:
                escolha = input("Digite 1 - cadastrar como professor | 2 - cadastrar como aluno: ")
                dominio_aluno = "@cesar.school"
                dominio_professor= "@gmail.com"
                if escolha == "1":
                    tentando_entrar_2 = True
                    while True:
                        login = input("Digite seu email: ").strip()
                        senha = getpass("Digite sua senha: ",stream=None)
                        if dominio_professor == login[-len(dominio_professor):] and login not in lista_emails_professores:
                            add_professor(login, senha)
                            print("Professor cadastrado.")
                            subprocess.run(["python","adm_tela.py"])
                            break
                        elif login in lista_emails_professores:
                            print("Email já cadastrado! Tente efetuar o login.")
                            break
                        else:
                            print("Digite um email válido.")
                elif escolha == "2":
                    tentando_entrar_2 = True
                    while True:
                        login = input("Digite seu email: ").strip()
                        senha = getpass("Digite sua senha: ",stream=None)
                        if dominio_aluno == login[-len(dominio_aluno):] and login not in lista_emails_alunos:
                            add_aluno(login, senha)
                            print("Aluno cadastrado.")
                            subprocess.run(["python","aluno_tela.py"])
                            break
                        elif login in lista_emails_alunos:
                            print("Email já cadastrado! Tente efetuar o login.")
                            break
                        else:
                            print("Digite um email válido.")
                else:
                    print("Opção inválida!")
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Digite apenas 1 ou 2.")

file_adm.close()
file_alunos.close()