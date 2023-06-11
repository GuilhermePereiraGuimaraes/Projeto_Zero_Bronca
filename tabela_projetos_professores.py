from rich.console import Console
from rich.table import Table

arquivo = open("doc_dados\projetos.txt","r")
lista_linhas = arquivo.readlines()

lista_projetos = []

for linha in lista_linhas:
    projeto = linha.replace("\n","")
    projeto = list(projeto.split("|"))
    lista_projetos.append(projeto)

tabela = Table(title="Projetos")
colunas = ["Cod. Projeto","Num. Grupo", "Nome do Grupo", "Período", "Temática do Projeto", "Nota", "Cliente", "Link"]

for coluna in colunas:
    tabela.add_column(coluna, justify="center", style="color(2)")

for linha in lista_projetos:
    tabela.add_row(*linha)

Console().print(tabela)
arquivo.close()