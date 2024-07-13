arquivo = open('produtos-vendas.csv', 'w')

arquivo.write("Código do Produto, Nome do Produto, Preço, Quantidade, Preço, Preço Unitário, Total da Compra\n")

csv_files = ['produtos.csv', 'vendas.csv']

for filename in csv_files:
    with open(filename) as open_csv:
        first_row = True 
        for line in open_csv:
            if first_row:
                first_row = False
                continue

            arquivo.write(line.strip() + '\n')  

arquivo.close()