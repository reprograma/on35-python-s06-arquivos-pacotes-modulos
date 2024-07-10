import pandas as pd

caminho_arquivo = "atv-casa.xlsx"
# Carregar todas as planilhas do arquivo Excel em um dicionário de DataFrames
# todas_abas = pd.read_excel(caminho_arquivo, sheet_name=None)

todas_abas = pd.read_excel(caminho_arquivo, sheet_name=None)  # Todas as informações de toda planilha (todas as abas)


# Lista para armazenar DataFrames processados
lista_dfs = []

# Iterar sobre todas as planilhas
for nome_aba, df in todas_abas.items():
    if nome_aba == 'nome_da_segunda_aba':  # Substitua pelo nome real da segunda aba
        df = df.iloc[1:]  # Remover o cabeçalho da segunda aba (assumindo que está na primeira linha)
        df.columns = todas_abas['nome_da_primeira_aba'].columns  # Definir as colunas para corresponder à primeira aba

    lista_dfs.append(df)

# Concatenar todos os DataFrames em um único DataFrame
df_combinado = pd.concat(lista_dfs, ignore_index=True)

# Salvar o DataFrame combinado em um novo arquivo Excel
novo_caminho_arquivo = "atv-cambinado-casa.xlsx"
df_combinado.to_excel(novo_caminho_arquivo, index=False)

print(f'arquivo criado com sucesso!')

# Funcionou
# import pandas as pd

# # Pegando apenas as informações desejadas:
# tabela = pd.read_excel("atv-casa.xlsx", sheet_name=None)  # Todas as informações de toda planilha (todas as abas)

# # Se você quiser exibir todas as abas da planilha
# for sheet_name, df in tabela.items():
#     print(f"--- {sheet_name} ---")
#     print(df)


# tabela = pd.read_excel("atv-casa.xlsx") #Poderia ter , sheet_name=0 para indicar que é a primeira aba
# display(tabela)

# tabela = pd.read_excel("atv-casa.xlsx", sheet_name=1)#segunda aba
# display(tabela)

# tabela = pd.read_excel("atv-casa.xlsx", sheet_name='notas_t2')
# display(tabela)

#Selecionando as colunas pelo nome da "coluna"
# tabela = pd.read_excel("atv-casa.xlsx", sheet_name='notas_t2',usecols="A:H")
# display(tabela)

#Pegando todas as informações de um arquivo
# tabela = pd.read_excel("atv-casa.xlsx", sheet_name=None)#todas as informações de toda planilha (todas as abas)
# display(tabela)

#Pegar determinada quantidade de linhas
# tabela = pd.read_excel("atv-casa.xlsx", sheet_name="notas_t1",skiprows=7)#aba notas_t1 e pula/desconsidera 7 linhas
# display(tabela)

#Pular linhas
# tabela = pd.read_excel("atv-casa.xlsx", sheet_name="notas_t1",nrows=11)#aba notas_t1 e pula/desconsidera 7 linhas
# display(tabela)

