import csv  


with open('venda_final', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)  
    
    for linha in leitor:
        print(linha)  

         #Não consegui fazer a leitura do arquivo e também não entendi muito bem qual eram as abas para fazer o merge.