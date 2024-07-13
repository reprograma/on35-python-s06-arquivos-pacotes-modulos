arquivo = open('notas-t1-t2.csv', 'w')

arquivo.write("Nome,Sobrenome,Nota 1Bimestre,Nota 2Bimestre, Nota 3Bimestre, Faltas 1Bimestre, Faltas 2Bimestre, Faltas 3Bimestre\n")

csv_files = ['notas-t1.csv', 'notas-t2.csv']

for filename in csv_files:
    with open(filename) as open_csv:
        first_row = True 
        for line in open_csv:
            if first_row:
                first_row = False
                continue

            arquivo.write(line.strip() + '\n')  

arquivo.close()