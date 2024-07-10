import csv  

with open('maio_abril_2024.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile) 
    for linha in leitor:
        print(linha)
