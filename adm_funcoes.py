from rich.console import Console
from rich.table import Table


def add_aluno(login, senha):
    arquivo = open("doc_dados\alunos.txt","a")
    aluno_acesso = f"{login} {senha}\n"
    arquivo.write(aluno_acesso)
    arquivo.close()

def add_professor(login,senha):
    arquivo = open("doc_dados\administradores.txt","a")
    adm_acesso = f"{login} {senha}\n"
    arquivo.write(adm_acesso)
    arquivo.close()

def remover_aluno(login, senha):
    arquivo = open("doc_dados\alunos.txt","r")
    aluno = f"{login} {senha}\n"
    file_list = arquivo.readlines()
    arquivo.close()
    arquivo = open("doc_dados\alunos.txt","w")
    for x in file_list:
        if x == aluno:
            continue
        arquivo.write(x)
    arquivo.close()

def remover_professor(login, senha):
    arquivo = open("doc_dados\administradores.txt","r")
    professor = f"{login} {senha}\n"
    file_list = arquivo.readlines()
    arquivo.close()
    arquivo = open("doc_dados\administradores.txt","w")
    for x in file_list:
        if x == professor:
            continue
        arquivo.write(x)
    arquivo.close()

def gerar_codigo_grupo():
    from random import randint
    from math import pi

    arquivo = open("doc_dados\projetos.txt","r")
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
    arquivo = open("doc_dados\projetos.txt","a")
    projeto = f"{codigo}|{num_gp}|{nome_gp}|{periodo}|{tematica}|{nota}|{cliente}|{link}\n"
    print(projeto[:-2])
    arquivo.write(projeto)
    arquivo.close()

def remover_projeto(codigo):
    arquivo = open("doc_dados\projetos.txt","r")
    lista_projetos = arquivo.readlines()
    arquivo.close()
    arquivo = open("doc_dados\projetos.txt","w")
    for p in lista_projetos:
        if p[:5] == codigo:
            continue
        arquivo.write(p)
    arquivo.close()

def filtro_cod_projeto(codigo,colunas):
    arquivo = open("doc_dados\projetos.txt","r")
    todos_projetos = arquivo.readlines()
    
    projetos_contados = 0
    projetos_filtrados = Table(title="Projetos")
    
    for coluna in colunas:
        projetos_filtrados.add_column(coluna, justify="center", style="color(2)")

    for pl in todos_projetos:
        projeto = pl.replace("\n","")
        projeto = list(projeto.split("|"))
        if codigo == projeto[0]:
            projetos_contados += 1
            projetos_filtrados.add_row(*projeto)
            break
    
    arquivo.close()
    
    if projetos_contados > 0:
        return projetos_filtrados
    else:
        return "Nenhum projeto encontrado!"    
    
