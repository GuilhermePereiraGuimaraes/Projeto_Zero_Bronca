def add_aluno(login, senha):
    arquivo = open("alunos.txt","a")
    aluno_acesso = f"{login} {senha}\n"
    arquivo.write(aluno_acesso)
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
    

escolha_acao = int(input('''O que você gostaria de fazer ?
1 - Add aluno/professor
2 - Remover aluno/professor
3 - Filtrar projetos
4 - Modificar projetos (adicionar, excluir, alterar informções)
5 - Sair
Sua escolha: '''))

if escolha_acao == 1:
    escolha_acao = int(input("Digite 1 - aluno | 2 - professor: "))
    if escolha_acao==1:
        login_aluno = input("Digite o login do aluno: ")
        senha_aluno = input("Digite a senha do aluno: ")
        add_aluno(login_aluno, senha_aluno)
    elif escolha_acao == 2:
        pass
    else:
        pass
elif escolha_acao ==2:
    login_aluno = input("Digite o login do aluno: ")
    senha_aluno = input("Digite a senha do aluno: ")
    remover_aluno(login_aluno, senha_aluno)
else:
    pass