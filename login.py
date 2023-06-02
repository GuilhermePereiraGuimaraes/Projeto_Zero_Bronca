from getpass import getpass
from adm_funcoes import add_aluno,add_professor
import subprocess

# Essa primeira função coloca os valores de um arquivo em um dicionário
def converter_file_dict(file,dic):
    for x in file.readlines():
        lista = x.split(" ")
        lista[1] = lista[1][:len(lista[1])-1]
        dic.update({lista[0]:lista[1]})

# Essa função busca checar a válidade do login e senha com base em um dicionário especificado
def analise_login_senha(login, senha, dic):
    login_dic = dic.keys()    

    if login in login_dic:
        if dic[login]==senha:
            return True
        else:
            print("Senha incorreta")
    else:
        print("Login incorreto")
    
    return False


# Aqui abrimos o arquivo apenas para leitura
file_adm = open("administradores.txt","r")
file_alunos = open("alunos.txt","r")

dicionario_adms = {}
dicionario_alunos={}
dicionario_escolhido= {}

converter_file_dict(file_adm,dicionario_adms)

print(dicionario_adms)

# Calculamos a quantidade de linhas do arquivo para podermos utilizar esse dado no if logo abaixo
tamanho_linhas_alunos = len(file_alunos.readlines())
# O .seek(0) serve basicamente para resetarmos readline e readlines do arquivo
file_alunos.seek(0)

if tamanho_linhas_alunos > 0:
    converter_file_dict(file_alunos, dicionario_alunos)

print(dicionario_alunos)

try:
    entrar = int(input("Digite 1 - Para Logar | 2 - Para se cadastrar: "))
    if entrar == 1:
        escolha = input("Digite 1 - logar como professor | 2 - logar como aluno: ")
        #Logando como professor / administrador
        if escolha == "1":
            login = input("Digite seu email: ").strip()
            senha = getpass("Digite sua senha: ",stream=None)
            if analise_login_senha(login, senha, dicionario_adms):
                print("Login efeuado com sucesso!")
                subprocess.run(["python","adm_tela.py"])
            else:
                print("Login ou Senha inválidos!")
        #Logando como aluno
        elif escolha == "2":
            login = input("Digite seu email: ").strip()
            senha = getpass("Digite sua senha: ",stream=None)
            if analise_login_senha(login, senha, dicionario_alunos):
                print("Login efeuado com sucesso!")
                # subprocess.run(["python","aluno_tela.py"])
            else:
                print("Login ou Senha inválidos!")
        else:
            print("Opção inválida!")
    elif entrar == 2:
        escolha = input("Digite 1 - cadastrar como professor | 2 - cadastrar como aluno: ")
        if escolha == "1":
            pass
        elif escolha == "2":
            while True:
                dominio = "@cesar.school"
                login = input("Digite seu email: ").strip()
                senha = getpass("Digite sua senha: ",stream=None)
                if dominio == login[-len(dominio):]:
                    print("Legal!")
                else:
                    print("nâo legal")
        else:
            print("Opção inválida!")
    else:
        print("Opção inválida!")
except ValueError:
    print("Digite apenas 1 ou 2.")

# login = input("Digite seu email: ").strip()
# senha = getpass("Digite sua senha: ",stream=None)

# while True:
#     tipo_acesso = input("Digite o tipo de acesso: 1 - Professor / Adm ou 2 - Aluno: ")
#     try:
#         tipo_acesso = int(tipo_acesso)
#         if tipo_acesso == 1:
#             dicionario_escolhido = dicionario_adms
#             break
#         elif tipo_acesso == 2:
#             dicionario_escolhido=dicionario_alunos
#             break
#         else:
#             print("Valor de tipo de acesso inválido")
#     except ValueError:
#         print("O tipo de acesso só pode ser 1 ou 2")

# if analise_login_senha(login, senha,dicionario_escolhido):
#     print("Logado")


file_adm.close()
file_alunos.close()