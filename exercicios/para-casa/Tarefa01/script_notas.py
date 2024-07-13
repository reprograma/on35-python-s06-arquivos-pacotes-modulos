arquivo = open('notas.csv', 'w')

arquivo.write(
    "nome,sobrenome,nota1bimestre,nota2bimestre,nota3bimestre,faltas1bimestre,faltas2bimestre,faltas3bimestre\n")

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
