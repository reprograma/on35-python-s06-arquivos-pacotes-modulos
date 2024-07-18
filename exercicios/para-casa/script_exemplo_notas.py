# Abre/Criar o arquivo 'exercicio01-notas_t1_exercicio01-notas_t2.csv' para escrita
arquivo = open('exercicio01-notas_t1_exercicio01-notas_t2.csv', 'w')

# Cria a linha de cabeçalho de saída
arquivo.write("id,mean\n")

# Lista de arquivos CSV que serão mesclados
csv_files = ['exercicio01-notas_t1.csv', 'exercicio01-notas_t2.csv']

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