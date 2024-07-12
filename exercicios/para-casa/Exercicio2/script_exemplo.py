
arquivo = open('venda_Final.csv', 'w')

arquivo.write("Código do Produto,Quantidade,Preço,Total,Total da Compra\n")


csv_files = ['sessao_vendas.csv','vendas.csv']

for filename in csv_files:
    
    with open(filename) as open_csv:
        first_row = True  
        for line in open_csv:
            
            if first_row:
                first_row = False
                continue
            
            arquivo.write(line.strip() + '\n')  

arquivo.close()