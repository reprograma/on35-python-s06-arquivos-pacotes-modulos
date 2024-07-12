import csv  
with open('exercicio01_t1_t2.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)  

    for linha in leitor:
        print(linha)  
