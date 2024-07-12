arquivo = open('maio_abril_2024.csv', 'w')
arquivo.write("id,mean\n")
csv_files = ['abril-2024.csv', 'maio2-2024.csv']
for filename in csv_files:
  with open(filename) as open_csv:
      first_row = True  
      for line in open_csv:
          # Ignora a linha de cabeçalho
          if first_row:
              first_row = False
              continue
          arquivo.write(line.strip() + '\n')  

arquivo.close()
