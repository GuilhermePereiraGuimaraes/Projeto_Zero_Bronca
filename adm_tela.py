import adm_funcoes


escolha_acao = int(input('''O que você gostaria de fazer ?
1 - Add aluno/professor
2 - Remover aluno/professor
3 - Modificar projetos (adicionar, excluir, alterar informções)
4 - Filtrar projetos
5 - Sair
Sua escolha: '''))

if escolha_acao == 1:
    try:
        escolha_acao = int(input("Digite 1 - aluno | 2 - professor: "))
        if escolha_acao==1:
            login_aluno = input("Digite o login do aluno: ")
            senha_aluno = input("Digite a senha do aluno: ")
            adm_funcoes.add_aluno(login_aluno, senha_aluno)
        elif escolha_acao == 2:
            login_professor = input("Digite o login do professor: ")
            senha_professor = input("Digite a senha do professor: ")
            adm_funcoes.add_professor(login_professor, senha_professor)
        else:
            print("Escolha inválida!")
    except ValueError:
        print("Valor inválido!")

elif escolha_acao ==2:
    try:
        escolha_acao = int(input("Digite 1 - aluno | 2 - professor: "))
        if escolha_acao==1:
            login_aluno = input("Digite o login do aluno: ")
            senha_aluno = input("Digite a senha do aluno: ")
            adm_funcoes.remover_aluno(login_aluno, senha_aluno)
        elif escolha_acao == 2:
            login_professor = input("Digite o login do professor: ")
            senha_professor = input("Digite a senha do professor: ")
            adm_funcoes.remover_professor(login_professor, senha_professor)
        else:
            print("Escolha inválida!")
    except ValueError:
        print("Valor inválido!")
else:
    pass