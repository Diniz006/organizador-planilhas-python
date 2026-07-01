import pandas as pd


def organizar_planilha(arquivo_entrada, arquivo_saida):
    # Lê a planilha bagunçada
    planilha = pd.read_excel(arquivo_entrada)

    linhas_antes = len(planilha)

    print("PLANILHA ORIGINAL")
    print(planilha)

    # Remove linhas completamente vazias
    planilha = planilha.dropna(how="all")

    linhas_depois = len(planilha)
    linhas_removidas = linhas_antes - linhas_depois

    # Padroniza os nomes das colunas
    planilha.columns = planilha.columns.str.strip().str.lower().str.replace(" ", "_")

    # Remove espaços extras em textos
    for coluna in planilha.columns:
        if planilha[coluna].dtype == "object":
            planilha[coluna] = planilha[coluna].str.strip()

    # Padroniza e-mails para letras minúsculas e remove espaços
    planilha["email"] = planilha["email"].str.strip().str.lower()

    # Padroniza status para letras minúsculas e remove espaços
    planilha["status"] = planilha["status"].str.strip().str.lower()

    # Padroniza nomes removendo espaços extras
    planilha["nome"] = planilha["nome"].str.strip()

    # Corrige o telefone para texto sem notação científica
    planilha["telefone"] = planilha["telefone"].astype("Int64").astype(str)

    # Salva a planilha limpa em um novo arquivo
    planilha.to_excel(arquivo_saida, index=False)

    print("-" * 50)
    print("PLANILHA LIMPA")
    print(planilha)
    print("-" * 50)

    print("Planilha organizada com sucesso!")
    print()
    print("Resumo:")
    print(f"- Linhas antes da limpeza: {linhas_antes}")
    print(f"- Linhas depois da limpeza: {linhas_depois}")
    print(f"- Linhas removidas: {linhas_removidas}")
    print(f"- Arquivo gerado: {arquivo_saida}")


organizar_planilha("clientes_baguncados.xlsx", "clientes_organizados.xlsx")