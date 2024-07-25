import csv  # Importa o módulo csv, que fornece funcionalidades para ler e escrever arquivos CSV

# Abre o arquivo 'abril_maio_2024.csv' para leitura, usando o gerenciador de contexto 'with'
# O parâmetro 'newline=""' é usado para evitar problemas com quebras de linha
# O parâmetro 'encoding="utf-8"' garante que o arquivo seja lido usando a codificação UTF-8
with open('abril_maio_2024.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)  # Cria um objeto leitor CSV que itera sobre as linhas do arquivo

    # Itera sobre cada linha do objeto leitor CSV
    for linha in leitor:
        print(linha)  # Imprime cada linha lida do arquivo CSV
        # Cada linha é uma lista de strings, onde cada elemento da lista corresponde a um campo no CSV
