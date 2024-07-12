
arquivo = open('notas_t1_notas_t2.csv', 'w')

arquivo.write("Nome,Sobrenome,Nota 1 Bimestre,Nota 2 Bimestre,Nota 3 Bimestre,Faltas 1 Bimestre,Faltas 2 Semestre,Faltas 3Bimestre\n")

csv_files = ['notas_t1.csv', 'notas_t2.csv']


for filename in csv_files:
  
    with open(filename) as open_csv:
        first_row = True  
        for line in open_csv:
            if first_row:
                first_row = False
                continue
            
            arquivo.write(line.strip() + '\n')  


arquivo.close()