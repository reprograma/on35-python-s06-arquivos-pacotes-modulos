# Abre/Criar o arquivo 'exercicios-grupo2-produtos_exercicios-grupo2-vendas.csv' para escrita
with open('exercicios-grupo2-produtos_exercicios-grupo2-vendas.csv', 'w', encoding='utf-8') as arquivo:
    # Cria a linha de cabeçalho de saída (ajuste conforme necessário)
    arquivo.write("id,mean\n")

    # Lista de arquivos CSV que serão mesclados
    csv_files = ['exercicios-grupo2-produtos.csv', 'exercicios-grupo2-vendas.csv']

    # Itera por todos os arquivos CSV que você deseja mesclar
    for filename in csv_files:
        # Abre cada arquivo CSV no modo de leitura com a codificação correta
        with open(filename, encoding='utf-8') as open_csv:
            first_row = True  # Variável para identificar a primeira linha (cabeçalho)
            for line in open_csv:
                # Ignora a linha de cabeçalho
                if first_row:
                    first_row = False
                    continue
                # Adiciona todas as outras linhas dos dados CSV ao arquivo de saída
                arquivo.write(line.strip() + '\n')  # Remove espaços em branco das extremidades e adiciona uma nova linha