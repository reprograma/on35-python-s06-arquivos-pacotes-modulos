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
        first_row = True  # Variável para identificar a primeira linha (cabeçalho)
        for line in open_csv:
            # Ignora a linha de cabeçalho
            if first_row:
                first_row = False
                continue
            # Adiciona todas as outras linhas dos dados CSV ao arquivo de saída
            arquivo.write(line.strip() + '\n')  # Remove espaços em branco das extremidades e adiciona uma nova linha

# Fecha o arquivo de saída
arquivo.close()