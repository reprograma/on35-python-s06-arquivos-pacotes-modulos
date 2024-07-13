# Abre/Criar o arquivo 'maio_abril_2024.csv' para escrita
arquivo = open('abril_maio_2024.csv', 'w')

# Cria a linha de cabeçalho de saída
arquivo.write("id,mean\n")

# Lista de arquivos CSV que serão mesclados
csv_files = ['abril-2024.csv', 'maio-2024.csv']

# Itera por todos os arquivos CSV que você deseja mesclar
for filename in csv_files:
    # Abre cada arquivo CSV no modo de leitura
    with open(filename) as open_csv:
        # Variável para identificar a primeira linha (cabeçalho)
        first_row = True
        for line in open_csv:
            # Ignora a linha de cabeçalho
            if first_row:  # if first_row == True:
                first_row = False
                continue
            # Adiciona todas as outras linhas dos dados CSV ao arquivo de saída
            # Remove espaços em branco das extremidades e adiciona uma nova linha
            arquivo.write(line.strip() + '\n')

# Fecha o arquivo de saída
arquivo.close()
