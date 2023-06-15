from rich.console import Console
from rich.table import Table

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
            return "Senha incorreta"
    return "Login inexistente"


def add_aluno(login, senha):
    arquivo = open("doc_dados\\alunos.txt","a")
    aluno_acesso = f"{login} {senha}\n"
    arquivo.write(aluno_acesso)
    arquivo.close()

def add_professor(login,senha):
    arquivo = open("doc_dados\\administradores.txt","a")
    adm_acesso = f"{login} {senha}\n"
    arquivo.write(adm_acesso)
    arquivo.close()

def remover_aluno(login):
    arquivo = open("doc_dados\\alunos.txt","r")
    # aluno = f"{login}"
    file_list = arquivo.readlines()
    dicionario_alunos = {}
    arquivo.seek(0)
    converter_file_dict(arquivo, dicionario_alunos)
    arquivo.close()
    logins_alunos = dicionario_alunos.keys()
    if login in logins_alunos:
        aluno = f"{login} {dicionario_alunos[login]}\n"
        arquivo = open("doc_dados\\alunos.txt","w")
        for x in file_list:
            if x == aluno:
                continue
            arquivo.write(x)
        arquivo.close()
        print("Aluno excluído!")
    else:
        print("Aluno inexistente!")

def remover_professor(login):
    arquivo = open("doc_dados\\administradores.txt","r")
    # aluno = f"{login}"
    file_list = arquivo.readlines()
    dicionario_prof = {}
    arquivo.seek(0)
    converter_file_dict(arquivo, dicionario_prof)
    arquivo.close()
    logins_profs = dicionario_prof.keys()
    if login in logins_profs:
        professor = f"{login} {dicionario_prof[login]}\n"
        arquivo = open("doc_dados\\administradores.txt","w")
        for x in file_list:
            if x == professor:
                continue
            arquivo.write(x)
        arquivo.close()
        print("Professor excluído!")
    else:
        print("Professor inexistente!")

def gerar_codigo_grupo():
    from random import randint
    from math import pi

    arquivo = open("doc_dados\\projetos.txt","r")
    ler_arquivo = arquivo.read()
    codigo =""

    while True:
        numero = round(pi * randint(1, 10000000))
        codigo = str(numero)[:5]
        if codigo in ler_arquivo:
            continue
        break

    return codigo


def add_projeto(num_gp, nome_gp, periodo, tematica, nota, cliente,link):
    codigo = gerar_codigo_grupo()
    arquivo = open("doc_dados\\projetos.txt","a")
    projeto = f"{codigo}|{num_gp}|{nome_gp}|{periodo}|{tematica}|{nota}|{cliente}|{link}\n"
    print(projeto[:-2])
    arquivo.write(projeto)
    arquivo.close()

def remover_projeto(codigo):
    arquivo = open("doc_dados\\projetos.txt","r")
    lista_projetos = arquivo.readlines()
    arquivo.close()
    arquivo = open("doc_dados\\projetos.txt","w")
    for p in lista_projetos:
        if p[:5] == codigo:
            continue
        arquivo.write(p)
    arquivo.close()

def filtro_projeto (dado,coluna_especifica,colunas):
    colunas_nomes = [2, 4, 6]
    arquivo = open("doc_dados\\projetos.txt","r")
    todos_projetos = arquivo.readlines()
    
    projetos_contados = 0
    projetos_filtrados = Table(title="Projetos")
    
    for coluna in colunas:
        projetos_filtrados.add_column(coluna, justify="center", style="color(2)")

    if coluna_especifica in colunas_nomes:
        for pl in todos_projetos:
            projeto = pl.replace("\n","")
            projeto = list(projeto.split("|"))
            if dado.lower() == projeto[coluna_especifica].lower():
                projetos_contados += 1
                projetos_filtrados.add_row(*projeto)
    else:
        if coluna_especifica == 1:
            for pl in todos_projetos:
                projeto = pl.replace("\n","")
                projeto = list(projeto.split("|"))
                if dado == int(projeto[coluna_especifica]):
                    projetos_contados += 1
                    projetos_filtrados.add_row(*projeto)
        elif coluna_especifica == 5:
            for pl in todos_projetos:
                projeto = pl.replace("\n","")
                projeto = list(projeto.split("|"))
                if dado == float(projeto[coluna_especifica]):
                    projetos_contados += 1
                    projetos_filtrados.add_row(*projeto)
        else:
            for pl in todos_projetos:
                projeto = pl.replace("\n","")
                projeto = list(projeto.split("|"))
                if dado == projeto[coluna_especifica]:
                    projetos_contados += 1
                    projetos_filtrados.add_row(*projeto)
    
    arquivo.close()
    
    if projetos_contados > 0:
        return projetos_filtrados
    else:
        return "Nenhum projeto encontrado!"
