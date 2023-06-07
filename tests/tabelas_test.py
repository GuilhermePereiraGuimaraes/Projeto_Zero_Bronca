from rich.console import Console
from rich.table import Table

table = Table(title="Pessoas")

colunas = ["Primeiro Nome", "Sobrenome", "Idade"]
linhas = [
    ["John","Doe","45"],
    ["Guilherme", "Guimarães", "22"],
    ["Mary", "Smith", "25"]
]

for coluna in colunas:
    table.add_column(coluna, justify="center",style="color(2)")

for linha in linhas:
    table.add_row(*linha)

# console = Console()
Console().print(table)