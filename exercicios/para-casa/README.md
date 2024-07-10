# Exercício de Casa 🏠 

**1.Abrir o drive com as planilhas que serão utilizadas:**
- Link do Drive: https://drive.google.com/drive/folders/1syeO00xDHh-JpW9583dXIWOHbvw2uF-w?usp=drive_link
- Nome da planilha: exercicios-grupo2
- Tratar os dados das abas Produtos e Vendas;
- Apagar os comentários antes de fazer o download;
- Criar uma pasta para receber o download dos arquivos;
- Fazer o download com os dados de Produtos e Vendas de forma separada em formato csv;
- Abrir o VSCODE;
- Utilizar o script dado em aula para mergear as planilhas;
- Verificar o merge com o script de leitura.

---
**2. para mergear os arquivos CSV em python:**
  ```
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
```
**3.Leitura dos Dados**:

```
import csv  

with open('maio_abril_2024.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile) 
    for linha in leitor:
        print(linha)
```
**Arquivos e links extras**
- [Módulo em Python](https://docs.python.org/pt-br/3/tutorial/modules.html)
- [Tabelas Dinâmicas](https://kondado.com.br/blog/blog/2023/04/17/criando-uma-tabela-dinamica-no-google-sheets/)
- [Video sobre Tabelas Dinâmicas](https://www.youtube.com/watch?v=QdW78AkPjG0)


Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
