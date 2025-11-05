import sqlite3 as sql
import os 


def criarDB(nomeDB):
    if not os.path.exists(nomeDB):
        Conectar = sql.connect(nomeDB)
        Conectar.close()

        print("Banco de dados criado com sucesso!!\n\n")
    
    else:
        print("Banco de dados já existe\n\n")


    print("Banco de dados criado com sucesso!!\n\n","="*40, "\n")


def criarTabela(nomeDB, nomeTabela):
    Conectar = sql.connect(nomeDB)
    Cursor = Conectar.cursor()

    Cursor.execute(f''' CREATE TABLE IF NOT EXISTS {nomeTabela}''')

    Conectar.commit()
    Conectar.close()


def inserirDados(nomeDB, nomeTabela):
    Conectar = sql.connect(nomeDB)
    Cursor = Conectar.cursor()

    Cursor.execute(f''' CREATE TABLE IF NOT EXISTS {nomeTabela} (
                    Codigo INTEGER PRIMARY KEY,
                    Nome TEXT NOT NULL,
                    Sexo TEXT NOT NULL,
                    Salario REAL NOT NULL)''')
    
    codigoFuncionario = str(input("\nCódigo do funcionário:"))
    nomeFuncionario = str(input("\nNome do funcionário:"))
    sexoFuncionario = str(input("\nSexo do funcionário:"))
    salarioFuncionario = float(input("\nSalário do funcionário:"))

    Cursor.execute(f''' INSERT INTO {nomeTabela} 
                   (Codigo, 
                    Nome, 
                    Sexo, 
                    Salario)
                    VALUES (?,?,?,?) ''' , (codigoFuncionario, nomeFuncionario, sexoFuncionario, salarioFuncionario))

    Conectar.commit()
    Conectar.close()


def lerDB(nomeDB, nomeTabela):
    Conectar = sql.connect(nomeDB)
    Cursor = Conectar.cursor()

    Cursor.execute(f''' SELECT * FROM {nomeTabela} ''')

    print ("\nRelação dos funcionários:\n","="*40, "\n")

    print("{:>12} {:<25} {:<10} {:>12}".format("Codigo", "Nome", "Sexo", "Salário"))

    dados = Cursor.fetchall()

    for linha in dados:
        print("{:>12} {:<25} {:<10} {:>12}".format(linha[0], linha[1], linha[2], linha[3]))

    print("="*40, "\n")
    Conectar.close()


##MAIN
i = True
while i == True:
    try:
        menu = int(input("Escolha uma opção:\n0 - Criar Tabela\n1 - Inserir Dados\n2 - Ler Dados\n3 - Sair\n"))
        
        match menu:
            case 0:
                nomeDB = str(input("Nome do banco de dados (EX.db):"))
                if not os.path.exists(nomeDB):
                    criarDB(nomeDB)
                else :
                    print("\nBanco de dados já existe!!\n\n","="*40, "\n")

            case 1:
                nomeDB = str(input("\nNome do banco de dados o qual deseja criar uma tabela (EX.db):"))
                if not os.path.exists(nomeDB):
                    print("\nBanco de dados não encontrado!!\nCrie o banco primeiro\n")
                    breakpoint()
                else: 
                    nomeTabela = str(input("\nNome da tabela:"))
                    criarTabela(nomeDB, nomeTabela)

            case 2:
                nomeDB = str(input("\nNome do banco de dados o qual deseja inserir dados (EX.db):"))
                if not os.path.exists(nomeDB):
                    print("\nBanco de dados não encontrado!!\nCrie o banco e a tabela primeiro\n")
                    breakpoint()

                else:
                    y = True
                    while y == True:
                        try:
                            inserirDados()
                            repetir = int(input("\nDeseja inserir mais um funcionário? SIM = 0 || NÃO = 1:\n"))
                            if repetir == 1:
                                y = False
                        except Exception as Erro:
                            print(TypeError)

            case 3:
                print("\nCerto\nAté mais\nO programa sera encerrado!!")
                i = False
                breakpoint()

            case _:
                print("\nValor invalido")
                breakpoint()
        
    except Exception as Erro:
        print(TypeError, Erro)