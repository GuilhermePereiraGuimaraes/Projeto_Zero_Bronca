import adm_funcoes


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
                            adm_funcoes.add_projeto(num_gp, nome_gp, ano_periodo, tematica, nota, cliente, link)
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
                adm_funcoes.remover_projeto(codigo)
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
    pass
else:
    pass