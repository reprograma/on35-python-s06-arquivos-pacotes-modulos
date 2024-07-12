import csv  


with open('notas_t1_notas_t2.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)  
    
    for linha in leitor:
        print(linha)  