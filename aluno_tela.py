from rich.console import Console
from rich.table import Table
import funcoes_projeto
import subprocess

while True:
    escolha_acao = input('''O que você gostaria de fazer ?
    1 - Filtrar projetos
    2 - Sair
    Sua escolha: ''')

    if escolha_acao == "1":
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
    elif escolha_acao == "2":
        print("Saindo...")
        break
    else:
        print("Escolha inválida!")