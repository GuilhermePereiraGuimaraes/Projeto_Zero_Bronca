from rich.console import Console
from rich.table import Table
import funcoes_projeto
import subprocess

while True:
    escolha_acao = input('''O que você gostaria de fazer ?
    1 - Modificar projetos (adicionar ou excluir)
    2 - Filtrar projetos
    3 - Remover aluno/professor
    4 - Sair
    Sua escolha: ''')

    if escolha_acao == "1":
        try:
            escolha_proj_acao = int(input("Digite 1 - adicionar projeto | 2 - excluir projeto: "))
            if escolha_proj_acao == 1:
                try:
                    num_gp = int(input("Digite o número do grupo: "))
                    nome_gp = input("Digite o nome do grupo: ").strip().title()
                    
                    ano_periodo = input("Digite o ano e período: ")
                    ano = ano_periodo[:-2]
                    semestre = ano_periodo[-1]
                    ponto_separacao = ano_periodo[-2]

                    if ano.isnumeric() and ponto_separacao == "." and (semestre=="1" or semestre == "2"):
                        tematica = input("Digite a temática do projeto: ").capitalize()
                        try:
                            nota = float(input("Digite a nota do grupo: "))
                            if nota>10 or nota<0:
                                print("Nota inválida!")
                            else:
                                cliente = input("Digite o nome do cliente: ").strip().title()
                                link = input("Digite o link do repositório: ").strip()
                                funcoes_projeto.add_projeto(num_gp, nome_gp, ano_periodo, tematica, nota, cliente, link)
                                print("Projeto adicionado!")
                        except ValueError:
                            print("Valor de nota inválido!")
                    else:
                        print("Ano e/ou período inválido.")
                except ValueError:
                    print("Digite apenas inteiros para o número do grupo")
            elif escolha_proj_acao == 2:
                codigo = input("Digite o codigo do projeto: ")
                if codigo.isnumeric():
                    arquivo = open("doc_dados\projetos.txt","r")
                    tamanho_txt = len(arquivo.readlines())
                    arquivo.close()
                    funcoes_projeto.remover_projeto(codigo)
                    arquivo = open("doc_dados\projetos.txt","r")
                    novo_tamanho = len(arquivo.readlines())
                    arquivo.close()

                    if tamanho_txt == novo_tamanho:
                        print("Projeto inexistente")
                    else:
                        print("Projeto excluído!")
                else:
                    print("Digite apenas números para o código.")
            else:
                print("Escolha inválida!")
        except ValueError:
            print("Valor inválido!")
    elif escolha_acao == "2":
        colunas = ["Cod. Projeto","Num. Grupo", "Nome do Grupo", "Período", "Temática do Projeto", "Nota", "Cliente", "Link"]
        
        subprocess.run(["python","tabela_projetos_professores.py"])
        escolha_filtro = input('''Qual filtro você gostaria de utilizar?
        1 - Código do projeto
        2 - Número do grupo
        3 - Nome do grupo
        4 - Período
        5 - Temática
        6 - Nota
        7 - Cliente
        Sua escolha: ''')
        if escolha_filtro == "1":
            codigo = input("Digite o codigo: ")
            projetos_filtrados = funcoes_projeto.filtro_projeto(codigo,0, colunas)
            Console().print(projetos_filtrados)
        elif escolha_filtro == "2":
            numero_grupo = int(input("Digite o número do grupo: "))
            projetos_filtrados = funcoes_projeto.filtro_projeto(numero_grupo,1, colunas)
            Console().print(projetos_filtrados)
        elif escolha_filtro == "3":
            nome_grupo = input("Digite o nome do grupo: ")
            projetos_filtrados = funcoes_projeto.filtro_projeto(nome_grupo,2, colunas)
            Console().print(projetos_filtrados)
        elif escolha_filtro == "4":
            periodo = input("Digite o periodo do projeto: ")
            projetos_filtrados = funcoes_projeto.filtro_projeto(periodo,3, colunas)
            Console().print(projetos_filtrados)
        elif escolha_filtro == "5":
            tematica = input("Digite a temática do projeto: ")
            projetos_filtrados = funcoes_projeto.filtro_projeto(tematica,4, colunas)
            Console().print(projetos_filtrados)
        elif escolha_filtro == "6":
            nota = float(input("Digite a nota do grupo: "))
            projetos_filtrados = funcoes_projeto.filtro_projeto(nota,5, colunas)
            Console().print(projetos_filtrados)
        elif escolha_filtro == "7":
            cliente = input("Digite o nome do cliente do projeto: ")
            projetos_filtrados = funcoes_projeto.filtro_projeto(cliente, 6, colunas)
            Console().print(projetos_filtrados)
        else:
            print("Escolha inválida!")
    elif escolha_acao == "3":
        opcao = input("Digite 1 - Aluno ou 2 - Professor: ").strip()
        if opcao == "1":
            login_aluno = input("Digite o email do aluno: ")
            funcoes_projeto.remover_aluno(login_aluno)
        elif opcao == "2":
            login_prof = input("Digite o email do professor: ")
            funcoes_projeto.remover_professor(login_prof)
        else:
            print("Opção inválida! ")
    elif escolha_acao == "4":
        print("Saindo...")
        break
    else:
        print("Escolha inválida!")