def add_aluno(login, senha):
    arquivo = open("alunos.txt","a")
    aluno_acesso = f"{login} {senha}\n"
    arquivo.write(aluno_acesso)
    arquivo.close()

def add_professor(login,senha):
    arquivo = open("administradores.txt","a")
    adm_acesso = f"{login} {senha}\n"
    arquivo.write(adm_acesso)
    arquivo.close()

def remover_aluno(login, senha):
    arquivo = open("alunos.txt","r")
    aluno = f"{login} {senha}\n"
    file_list = arquivo.readlines()
    arquivo.close()
    arquivo = open("alunos.txt","w")
    for x in file_list:
        if x == aluno:
            continue
        arquivo.write(x)
    arquivo.close()

def remover_professor(login, senha):
    arquivo = open("administradores.txt","r")
    professor = f"{login} {senha}\n"
    file_list = arquivo.readlines()
    arquivo.close()
    arquivo = open("administradores.txt","w")
    for x in file_list:
        if x == professor:
            continue
        arquivo.write(x)
    arquivo.close()

def gerar_codigo_grupo():
    from random import randint
    from math import pi

    arquivo = open("projetos.txt","r")
    ler_arquivo = arquivo.read()
    codigo =""

    while True:
        numero = round(pi * randint(1, 10000000))
        codigo = str(numero)[:5]
        if codigo in ler_arquivo:
            continue
        break

    return codigo


def add_projeto(num_gp, nome_gp, periodo, tematica, nota, cliente):
    pass

print(gerar_codigo_grupo())
